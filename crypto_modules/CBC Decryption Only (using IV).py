# Simple XOR-based block cipher for demonstration
def simple_block_decrypt(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

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

    # Remove padding
    padding_len = plaintext[-1]
    return plaintext[:-padding_len]

# Example use
key = b'12345678'
iv_hex = input("Enter IV (hex): ")
cipher_hex = input("Enter ciphertext (hex): ")

iv = bytes.fromhex(iv_hex)
ciphertext = bytes.fromhex(cipher_hex)

decrypted = cbc_decrypt(ciphertext, key, iv)
print("Decrypted:", decrypted.decode())
