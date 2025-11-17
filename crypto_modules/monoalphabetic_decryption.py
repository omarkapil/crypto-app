# Monoalphabetic Cipher - Decryption
# ملف فك التشفير بتقنية Monoalphabetic

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

def decrypt(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    table = str.maketrans(key, alpha)
    return text.lower().translate(table)

def process_text(text: str, seed: int = 12345) -> str:
    """
    Process text using Monoalphabetic Cipher Decryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        key = make_key(seed)
        decrypted = decrypt(text, key)
        result = f"Plaintext: {decrypted}\n\nSeed: {seed}\nKey: {key}"
        return result
    except Exception as e:
        return f"ERROR: Decryption failed: {str(e)}"

