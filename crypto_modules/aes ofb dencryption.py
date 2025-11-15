# decrypt_only.py
from Crypto.Cipher import AES
import base64

# ============================================================
#                     LCG Key Generator (must match encryption)
# ============================================================

def generate_lcg_key(seed=12345, a=1103515245, c=12345, m=2**31, length=16):
    x = seed % m
    key = bytearray()
    for _ in range(length):
        x = (a * x + c) % m
        key.append(x & 0xFF)
    return bytes(key)

# ============================================================
#                     AES-OFB Decryption (LCG Key)
# ============================================================

def decrypt_aes_ofb(ciphertext_b64: str, iv_b64: str) -> str:
    try:
        key = generate_lcg_key()  # Same as encryption
        iv = base64.b64decode(iv_b64)
        ct = base64.b64decode(ciphertext_b64)
    except Exception as e:
        raise ValueError(f"Invalid base64 input: {e}")

    cipher = AES.new(key, AES.MODE_OFB, iv)
    plaintext_bytes = cipher.decrypt(ct)
    return plaintext_bytes.decode('utf-8', errors='ignore')

# ============================================================
#                           RUN ONCE
# ============================================================

if __name__ == "__main__":
    print("=== AES-OFB DECRYPTION (LCG Key) ===\n")
    
    ciphertext = input("Enter ciphertext (base64): ").strip()
    iv = input("Enter IV (base64): ").strip()

    if not ciphertext or not iv:
        print("Error: Both fields are required!")
    else:
        try:
            plaintext = decrypt_aes_ofb(ciphertext, iv)
            print("\n--- PLAINTEXT ---")
            print(plaintext)
            print("\nDone.")
        except Exception as e:
            print(f"Decryption failed: {e}")