# AES-OFB encryption/decryption with user input
# Requires: pip install pycryptodome

import base64

try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    # Provide helpful error message
    def get_random_bytes(size):
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    # Define a dummy AES to prevent NameError (won't be used due to CRYPTO_AVAILABLE check)
    AES = None  # type: ignore

# ---------- Helper Functions ----------

def b64encode(b: bytes) -> str:
    """Convert bytes to base64 string (for display/storage)."""
    return base64.b64encode(b).decode('utf-8')

def b64decode(s: str) -> bytes:
    """Convert base64 string back to bytes."""
    return base64.b64decode(s.encode('utf-8'))

# ---------- AES-OFB Encryption/Decryption ----------

def ofb_encrypt(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    return cipher.encrypt(plaintext)

def ofb_decrypt(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    if not CRYPTO_AVAILABLE:
        raise ImportError("pycryptodome is not installed. Please run: pip install pycryptodome")
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    return cipher.decrypt(ciphertext)

# ---------- Flask Integration Function ----------

def process_text(text: str) -> str:
    """
    Process text using AES-OFB encryption for Flask app.
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
        ciphertext = ofb_encrypt(key, iv, plaintext_bytes)
        
        # Return formatted result with ciphertext, key, and IV (all in base64)
        result = f"Ciphertext: {b64encode(ciphertext)}\nKey: {b64encode(key)}\nIV: {b64encode(iv)}"
        return result
        
    except ImportError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

# ---------- Main Program (for standalone use) ----------

if __name__ == "__main__":
    print("=== AES-OFB Encryption / Decryption ===\n")
    print("Choose an option:")
    print("1. Encrypt text")
    print("2. Decrypt text")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        # --- Encryption ---
        plaintext = input("Enter plaintext: ").encode()

        key_option = input("Do you want to (g)enerate a random key or (m)anually enter one? [g/m]: ").lower()

        if key_option == "m":
            key_str = input("Enter key (as base64 or ASCII string): ")
            try:
                # Try to decode base64 first
                key = b64decode(key_str)
            except Exception:
                key = key_str.encode()
        else:
            key = get_random_bytes(32)  # AES-256

        iv = get_random_bytes(16)  # Always random IV for encryption

        ciphertext = ofb_encrypt(key, iv, plaintext)

        print("\n--- Encryption Complete ---")
        print("Ciphertext (base64):", b64encode(ciphertext))
        print("Key (base64):", b64encode(key))
        print("IV  (base64):", b64encode(iv))
        print("\n⚠ Save the key and IV to decrypt later.")

    elif choice == "2":
        # --- Decryption ---
        ciphertext_b64 = input("Enter ciphertext (base64): ")
        key_b64 = input("Enter key (base64): ")
        iv_b64 = input("Enter IV (base64): ")

        ciphertext = b64decode(ciphertext_b64)
        key = b64decode(key_b64)
        iv = b64decode(iv_b64)

        plaintext = ofb_decrypt(key, iv, ciphertext)

        print("\n--- Decryption Complete ---")
        print("Recovered plaintext:", plaintext.decode(errors='ignore'))

    else:
        print("Invalid choice. Please run again.")

