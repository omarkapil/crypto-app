# CBC Decryption
# ملف فك التشفير بتقنية CBC

def simple_block_decrypt(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

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

def process_text(text: str, iv_hex: str = "", key: bytes = b'12345678') -> str:
    """
    Process text using CBC Decryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    if not iv_hex:
        return "ERROR: IV is required for decryption."
    
    try:
        iv = bytes.fromhex(iv_hex)
        ciphertext = bytes.fromhex(text)
        decrypted = cbc_decrypt(ciphertext, key, iv)
        result = f"Plaintext: {decrypted.decode()}\n\nIV (hex): {iv_hex}\nKey: {key.decode()}"
        return result
    except Exception as e:
        return f"ERROR: Decryption failed: {str(e)}"

