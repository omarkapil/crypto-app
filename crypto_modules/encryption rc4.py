import base64

# === KSA (Key Scheduling Algorithm) ===
def ksa(key_bytes):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

# === LCG for Keystream Generation ===
def lcg_keystream(length, seed, a=1103515245, c=12345, m=256):
    stream = bytearray()
    x = seed
    for _ in range(length):
        x = (a * x + c) % m
        stream.append(x)
    return bytes(stream)

# === XOR Encryption ===
def xor_cipher(data_bytes, keystream):
    return bytes(b ^ k for b, k in zip(data_bytes, keystream))

# === Full RC4-LCG Encryption Process ===
def rc4_lcg_encrypt(plaintext, key):
    key_bytes = [ord(c) for c in key]
    S = ksa(key_bytes)
    seed = sum(S) % 256
    keystream = lcg_keystream(len(plaintext), seed)
    ciphertext_bytes = xor_cipher(plaintext, keystream)
    return base64.b64encode(ciphertext_bytes).decode('ascii')

# === Encryption Main ===
def encrypt_main():
    print("=== RC4-LCG Encryption ===")
    key = input("Enter key: ").strip()
    if not key:
        print("Error: Key cannot be empty.")
        return
    
    plaintext = input("Enter plaintext: ").strip()
    if not plaintext:
        print("Error: Plaintext cannot be empty.")
        return
    
    data_bytes = plaintext.encode('utf-8')
    ciphertext_b64 = rc4_lcg_encrypt(data_bytes, key)
    
    print("\n--- Encryption Result ---")
    print(f"Plaintext : {plaintext}")
    print(f"Key       : {key}")
    print(f"Ciphertext: {ciphertext_b64}")

if __name__ == "__main__":
    encrypt_main()
