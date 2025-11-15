from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# ============================================================
#                     LCG Key Generator (16 bytes = 128-bit)
# ============================================================

def generate_lcg_key(seed=12345, a=1103515245, c=12345, m=2**31, length=16):
    x = seed % m
    key = bytearray()
    for _ in range(length):
        x = (a * x + c) % m
        key.append(x & 0xFF)
    return bytes(key)

# ============================================================
#                     AES-OFB Encryption
# ============================================================

def encrypt_message(plaintext: str):
    # Generate fixed LCG key (for demo)
    key = generate_lcg_key()
    iv = get_random_bytes(16)  # Random IV every time

    cipher = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

    return {
        "AES Key (LCG, hex)": key.hex(),
        "IV (base64)": base64.b64encode(iv).decode('utf-8'),
        "Ciphertext (base64)": base64.b64encode(ciphertext).decode('utf-8')
    }

# ============================================================
#                           RUN ONCE
# ============================================================

if __name__ == "__main__":
    print("=== AES-OFB ENCRYPTION (LCG Key) ===\n")
    message = input("Enter your message: ").strip()

    if not message:
        print("Error: Message cannot be empty!")
    else:
        result = encrypt_message(message)
        print("\n--- ENCRYPTION RESULT ---")
        for key, value in result.items():
            print(f"{key}: {value}")
        print("\nDone.")
