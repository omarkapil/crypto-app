
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

def decrypt(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    table = str.maketrans(key, alpha)
    return text.lower().translate(table)

# --- Main ---
print("1) Encrypt\n2) Decrypt")
choice = input(">> ").strip()

if choice not in ("1", "2"):
    print("Invalid choice!")
    exit()

seed = int(input("Enter seed (int): "))
key = make_key(seed)
print("Key:", key)

text = input("Enter text: ")

if choice == "1":
    print("Encrypted:", encrypt(text, key))
else:
    print("Decrypted:", decrypt(text, key))
