# AES-OFB Decryption
# ملف فك التشفير بتقنية AES-OFB

try:
    from Crypto.Cipher import AES
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

def decrypt_aes_ofb(ciphertext_b64: str, iv_b64: str) -> str:
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    
    import base64
    try:
        key = generate_lcg_key()
        iv = base64.b64decode(iv_b64)
        ct = base64.b64decode(ciphertext_b64)
    except Exception as e:
        raise ValueError(f"Invalid base64 input: {e}")

    cipher = AES.new(key, AES.MODE_OFB, iv)
    plaintext_bytes = cipher.decrypt(ct)
    return plaintext_bytes.decode('utf-8', errors='ignore')

def process_text(text: str, iv_b64: str = "") -> str:
    """
    Process text using AES-OFB Decryption.
    """
    if not CRYPTO_AVAILABLE:
        return "ERROR: pycryptodome library is not installed. Please install it using: pip install pycryptodome"
    
    if not text:
        return "ERROR: Input text is empty."
    
    if not iv_b64:
        return "ERROR: IV is required for decryption."
    
    try:
        plaintext = decrypt_aes_ofb(text, iv_b64)
        result = f"Plaintext: {plaintext}\n\nIV (base64): {iv_b64}"
        return result
    except ValueError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Decryption failed: {str(e)}"

