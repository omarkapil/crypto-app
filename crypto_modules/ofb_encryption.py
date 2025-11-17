# AES-OFB Encryption
# ملف التشفير بتقنية AES-OFB

try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

def generate_lcg_key(seed=12345, a=1103515245, c=12345, m=2**31, length=16):
    x = seed % m
    key = bytearray()
    for _ in range(length):
        x = (a * x + c) % m
        key.append(x & 0xFF)
    return bytes(key)

def encrypt_message(plaintext: str):
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    
    key = generate_lcg_key()
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

    import base64
    return {
        "AES Key (LCG, hex)": key.hex(),
        "IV (base64)": base64.b64encode(iv).decode('utf-8'),
        "Ciphertext (base64)": base64.b64encode(ciphertext).decode('utf-8')
    }

def process_text(text: str) -> str:
    """
    Process text using AES-OFB Encryption.
    """
    if not CRYPTO_AVAILABLE:
        return "ERROR: pycryptodome library is not installed. Please install it using: pip install pycryptodome"
    
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        result = encrypt_message(text)
        output = f"Ciphertext (base64): {result['Ciphertext (base64)']}\n\n"
        output += f"IV (base64): {result['IV (base64)']}\n\n"
        output += f"AES Key (hex): {result['AES Key (LCG, hex)']}"
        return output
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

