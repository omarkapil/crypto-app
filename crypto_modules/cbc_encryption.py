# CBC Encryption
# ملف التشفير بتقنية CBC

def simple_block_encrypt(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

def lcg(seed, a, c, m, n):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)
    return numbers

def lcg_iv(seed, size=8):
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    numbers = lcg(seed, a, c, m, size)
    return bytes([n % 256 for n in numbers])

def cbc_encrypt(plaintext, key, seed):
    iv = lcg_iv(seed, size=len(key))
    block_size = len(key)
    ciphertext = b''

    padding_len = block_size - (len(plaintext) % block_size)
    plaintext += bytes([padding_len] * padding_len)

    prev_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        block_to_encrypt = bytes([b ^ pb for b, pb in zip(block, prev_block)])
        cipher_block = simple_block_encrypt(block_to_encrypt, key)
        ciphertext += cipher_block
        prev_block = cipher_block

    return iv, ciphertext

def process_text(text: str, key: bytes = b'12345678', seed: int = 42) -> str:
    """
    Process text using CBC Encryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        message = text.encode()
        iv, encrypted = cbc_encrypt(message, key, seed)
        result = f"Ciphertext (hex): {encrypted.hex()}\n\nIV (hex): {iv.hex()}\nKey: {key.decode()}"
        return result
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

