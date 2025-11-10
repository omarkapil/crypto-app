# Cipher Block Chaining (CBC) Mode
# AES-CBC encryption

import base64

try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Util.Padding import pad, unpad
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    def get_random_bytes(size):
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    AES = None  # type: ignore

def b64encode(b: bytes) -> str:
    """Convert bytes to base64 string."""
    return base64.b64encode(b).decode('utf-8')

def cbc_encrypt(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    """Encrypt plaintext using AES-CBC mode."""
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    # Pad the plaintext to be multiple of block size
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def cbc_decrypt(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    """Decrypt ciphertext using AES-CBC mode."""
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext

def process_text(text: str) -> str:
    """
    Process text using AES-CBC encryption for Flask app.
    Encrypts the text and returns base64 encoded ciphertext with key and IV.
    """
    if not CRYPTO_AVAILABLE:
        return "ERROR: pycryptodome library is not installed. Please install it using: pip install pycryptodome"
    
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        # Generate random key and IV for encryption
        key = get_random_bytes(32)  # AES-256
        iv = get_random_bytes(16)   # 16 bytes for AES block size
        
        # Encrypt the plaintext
        plaintext_bytes = text.encode('utf-8')
        ciphertext = cbc_encrypt(key, iv, plaintext_bytes)
        
        # Return formatted result with ciphertext, key, and IV (all in base64)
        result = f"Ciphertext: {b64encode(ciphertext)}\nKey: {b64encode(key)}\nIV: {b64encode(iv)}"
        return result
        
    except ImportError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

