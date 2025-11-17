# CTR (Counter) Mode Decryption
# ملف فك التشفير بتقنية AES-CTR

import base64

try:
    from Crypto.Cipher import AES
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

def b64decode(s: str) -> bytes:
    """Convert base64 string to bytes."""
    return base64.b64decode(s)

def ctr_decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
    """Decrypt ciphertext using AES-CTR mode."""
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def process_text(text: str, key_b64: str = "", nonce_b64: str = "") -> str:
    """
    Process text using AES-CTR Decryption.
    """
    if not CRYPTO_AVAILABLE:
        return "ERROR: pycryptodome library is not installed. Please install it using: pip install pycryptodome"
    
    if not text:
        return "ERROR: Input text is empty."
    
    if not key_b64 or not nonce_b64:
        return "ERROR: Key and Nonce are required for decryption."
    
    try:
        key = b64decode(key_b64)
        nonce = b64decode(nonce_b64)
        ciphertext = b64decode(text)
        plaintext = ctr_decrypt(key, nonce, ciphertext)
        
        result = f"Plaintext: {plaintext.decode('utf-8')}\n\nKey: {key_b64}\nNonce: {nonce_b64}"
        return result
    except ImportError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Decryption failed: {str(e)}"

