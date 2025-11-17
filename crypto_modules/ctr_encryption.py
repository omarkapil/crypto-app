# CTR (Counter) Mode Encryption
# ملف التشفير بتقنية AES-CTR

import base64

try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

def b64encode(b: bytes) -> str:
    """Convert bytes to base64 string."""
    return base64.b64encode(b).decode('utf-8')

def ctr_encrypt(key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
    """Encrypt plaintext using AES-CTR mode."""
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def process_text(text: str) -> str:
    """
    Process text using AES-CTR Encryption.
    """
    if not CRYPTO_AVAILABLE:
        return "ERROR: pycryptodome library is not installed. Please install it using: pip install pycryptodome"
    
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        key = get_random_bytes(32)
        nonce = get_random_bytes(8)
        plaintext_bytes = text.encode('utf-8')
        ciphertext = ctr_encrypt(key, nonce, plaintext_bytes)
        
        result = f"Ciphertext: {b64encode(ciphertext)}\n\nKey: {b64encode(key)}\nNonce: {b64encode(nonce)}"
        return result
    except ImportError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

