# Simple XOR-based block cipher for demonstration
def simple_block_encrypt(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

def simple_block_decrypt(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

# LCG (Linear Congruential Generator)
def lcg(seed, a, c, m, n):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)
    return numbers

# Convert LCG numbers to bytes for IV
def lcg_iv(seed, size=8):
    # Parameters for LCG
    a = 1664525
    c = 1013904223
    m = 2**32
    numbers = lcg(seed, a, c, m, size)
    iv = bytes([n % 256 for n in numbers])
    return iv

# CBC Encryption
def cbc_encrypt(plaintext, key, iv):
    block_size = len(key)
    ciphertext = b''
    
    # Pad plaintext to match block size
    padding_len = block_size - (len(plaintext) % block_size)
    plaintext += bytes([padding_len] * padding_len)
    
    prev_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        block_to_encrypt = bytes([b ^ pb for b, pb in zip(block, prev_block)])
        cipher_block = simple_block_encrypt(block_to_encrypt, key)
        ciphertext += cipher_block
        prev_block = cipher_block
    
    return ciphertext

# CBC Decryption
def cbc_decrypt(ciphertext, key, iv):
    block_size = len(key)
    plaintext = b''
    prev_block = iv
    
    for i in range(0, len(ciphertext), block_size):
        cipher_block = ciphertext[i:i+block_size]
        decrypted_block = simple_block_decrypt(cipher_block, key)
        plain_block = bytes([b ^ pb for b, pb in zip(decrypted_block, prev_block)])
        plaintext += plain_block
        prev_block = cipher_block
    
    padding_len = plaintext[-1]
    return plaintext[:-padding_len]

# Example usage
if _name_ == "_main_":
    key = b'12345678'  # 8-byte key
    seed = 42          # Seed for LCG
    iv = lcg_iv(seed, size=len(key))  # Generate IV using LCG
    
    message = input("Enter message: ").encode()

    encrypted = cbc_encrypt(message, key, iv)
    decrypted = cbc_decrypt(encrypted, key, iv)

    print("LCG-generated IV:", iv.hex())
    print("Encrypted (hex):", encrypted.hex())
    print("Decrypted:", decrypted.decode())
