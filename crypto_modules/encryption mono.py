# encrypt.py

def lcg(seed, n=26):
    a, c, m = 1664525, 1013904223, 2**32
    x = seed
    nums = []
    for _ in range(n):
        x = (a * x + c) % m
        nums.append(x)
    return nums

def make_key(seed):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    indices = sorted(range(26), key=lambda i: lcg(seed)[i])
    return ''.join(alpha[i] for i in indices)

def encrypt(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    table = str.maketrans(alpha, key)
    return text.lower().translate(table)

# === Encryption Main ===
def encrypt_main():
    print("=== Substitution Cipher - Encryption ===")
    
    try:
        seed = int(input("Enter seed (integer): ").strip())
    except ValueError:
        print("Error: Seed must be an integer.")
        return
    
    key = make_key(seed)
    print(f"Generated Key: {key}")
    
    text = input("Enter plaintext: ").strip()
    if not text:
        print("Error: Plaintext cannot be empty.")
        return
    
    encrypted = encrypt(text, key)
    
    print("\n--- Encryption Result ---")
    print(f"Plaintext : {text}")
    print(f"Seed      : {seed}")
    print(f"Key       : {key}")
    print(f"Ciphertext: {encrypted}")

if __name__ == "__main__":
    encrypt_main()
