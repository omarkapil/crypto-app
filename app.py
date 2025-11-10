from flask import Flask, render_template, request, jsonify
# استيراد جميع الدوال من ملفات التشفير

# Import all crypto modules
import crypto_modules.monoalphabetic_cipher as monoalphabetic
import crypto_modules.hill_cipher as hill
import crypto_modules.columnar_transposition as columnar
import crypto_modules.rc4 as rc4
import crypto_modules.mac as mac

# Import CBC with error handling
try:
    import crypto_modules.cbc as cbc
    CBC_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import cbc module: {e}")
    CBC_AVAILABLE = False
    class DummyCbc:
        @staticmethod
        def process_text(text):
            return "ERROR: CBC module is not available. Please install pycryptodome: pip install pycryptodome"
    cbc = DummyCbc()

# Import OFB with error handling
try:
    import crypto_modules.aes_ofb as ofb
    OFB_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import ofb module: {e}")
    OFB_AVAILABLE = False
    class DummyOfb:
        @staticmethod
        def process_text(text):
            return "ERROR: OFB module is not available. Please install pycryptodome: pip install pycryptodome"
    ofb = DummyOfb()

# Import CTR with error handling
try:
    import crypto_modules.ctr as ctr
    CTR_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import ctr module: {e}")
    CTR_AVAILABLE = False
    class DummyCtr:
        @staticmethod
        def process_text(text):
            return "ERROR: CTR module is not available. Please install pycryptodome: pip install pycryptodome"
    ctr = DummyCtr()

app = Flask(__name__)

# قائمة التقنيات (يُستخدم لإنشاء الأزرار ولربط نقطة النهاية بالدالة المناسبة)
CRYPTO_METHODS = {
    "Monoalphabetic": monoalphabetic.process_text,
    "Hill Cipher": hill.process_text,
    "Columnar Transposition": columnar.process_text,
    "RC4": rc4.process_text,
    "MAC": mac.process_text,
    "CBC": cbc.process_text,
    "OFB": ofb.process_text,
    "CTR": ctr.process_text
}

# ----------------------------------------------
# 🌐 نقاط النهاية (API Endpoints)
# ----------------------------------------------

# نقطة النهاية للواجهة الرئيسية (تخدم ملف HTML)
@app.route('/')
def index():
    # نمرر أسماء التقنيات إلى الـHTML لإنشاء الأزرار
    return render_template('index.html', methods=CRYPTO_METHODS.keys())

# نقطة النهاية الموحدة لمعالجة طلب التشفير/الهاش
@app.route('/api/process/<path:method_name>', methods=['POST'])
def process_text(method_name):
    # Convert URL method name to match dictionary keys
    # Replace hyphens with spaces and convert to title case for matching
    method_name_normalized = method_name.replace('-', ' ').replace('_', ' ')
    
    # Find matching key (case-insensitive, space/hyphen agnostic)
    method_key = None
    method_name_lower = method_name_normalized.lower()
    
    for key in CRYPTO_METHODS.keys():
        key_normalized = key.lower().replace(' ', '-')
        if key_normalized == method_name.lower() or key.lower() == method_name_lower:
            method_key = key
            break
    
    # If still not found, try title case match
    if method_key is None:
        method_key_candidate = method_name_normalized.title()
        if method_key_candidate in CRYPTO_METHODS:
            method_key = method_key_candidate
    
    # 1. التحقق من وجود التقنية
    if method_key is None or method_key not in CRYPTO_METHODS or CRYPTO_METHODS[method_key] is None:
        return jsonify({"error": f"Encryption method '{method_name}' not supported yet."}), 404

    # 2. استلام النص المُرسل من الواجهة الأمامية
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Input text is required."}), 400

    # 3. استدعاء الدالة المناسبة
    processor_function = CRYPTO_METHODS[method_key]
    
    try:
        result = processor_function(text)
        
        # إذا كان ناتج الدالة يبدأ بكلمة خطأ، نعتبرها خطأ ونرجعه بـ 500
        if result.startswith("ERROR:"):
            return jsonify({"error": result}), 500

        # 4. إرجاع النتيجة
        return jsonify({
            "method": method_key,
            "input_text": text,
            "output": result
        })
        
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred during processing: {str(e)}"}), 500


if __name__ == '__main__':
    print(f"Starting Flask server...")
    # 💡 يمكنك تغيير رقم البورت (5000) إذا كان مشغولاً
    app.run(debug=True, port=5000)