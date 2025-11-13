
import base64

# === KSA (Key Scheduling Algorithm) - ===
def ksa(key_bytes):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

# === LCG for Keystream Generation  ===
def lcg_keystream(length, seed, a=1103515245, c=12345, m=256):
    stream = bytearray()
    x = seed
    for _ in range(length):
        x = (a * x + c) % m
        stream.append(x)
    return bytes(stream)

# === XOR Encryption / Decryption ===
def xor_cipher(data_bytes, keystream):
    return bytes(b ^ k for b, k in zip(data_bytes, keystream))

# === Full RC4-LCG Process ===
def rc4_lcg_process(data_bytes, key_str):
    key_bytes = [ord(c) for c in key_str]
    S = ksa(key_bytes)
    seed = sum(S) % 256
    keystream = lcg_keystream(len(data_bytes), seed)
    return xor_cipher(data_bytes, keystream)

# === Main Interactive Menu ===
def main():
    print("RC4  ")
    print("Choose an option:")
    print("  1 - Encrypt")
    print("  2 - Decrypt")
    print()
    choice = input("Enter 1 or 2: ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice.")
        return

    key = input("\nEnter key: ").strip()
    if not key:
        print("Key cannot be empty.")
        return

    if choice == '1':
        plaintext = input("Enter plaintext: ").strip()
        if not plaintext:
            print("Plaintext cannot be empty.")
            return

        data_bytes = plaintext.encode('utf-8')
        ciphertext_bytes = rc4_lcg_process(data_bytes, key)
        ciphertext_b64 = base64.b64encode(ciphertext_bytes).decode('ascii')

        print("\n--- Result ---")
        print(f"Plaintext : {plaintext}")
        print(f"Key       : {key}")
        print(f"Ciphertext: {ciphertext_b64}")

    else:  # Decrypt
        cipher_b64 = input("\nEnter ciphertext (Base64): ").strip()
        if not cipher_b64:
            print("Ciphertext cannot be empty.")
            return

        try:
            ciphertext_bytes = base64.b64decode(cipher_b64)
        except Exception:
            print("Invalid Base64.")
            return

        decrypted_bytes = rc4_lcg_process(ciphertext_bytes, key)
        try:
            decrypted_text = decrypted_bytes.decode('utf-8')
        except UnicodeDecodeError:
            decrypted_text = f"[Binary: {decrypted_bytes.hex()}]"

        print("\n--- Result ---")
        print(f"Ciphertext: {cipher_b64}")
        print(f"Key       : {key}")
        print(f"Plaintext : {decrypted_text}")

if __name__ == "__main__":
    main()
