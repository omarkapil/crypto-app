# Columnar Transposition - Encryption
# ملف التشفير بتقنية Columnar Transposition

import math
import random

def encrypt_columnar(text: str, key: str) -> str:
    """Encrypt text using columnar transposition cipher."""
    text = text.replace(' ', '').upper()
    key = key.upper()
    
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    
    text += 'X' * (num_cols * num_rows - len(text))
    
    matrix = [list(text[i:i+num_cols]) for i in range(0, len(text), num_cols)]
    
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    key_order = [x[0] for x in sorted_key]
    
    ciphertext = []
    for col_idx in key_order:
        for row in matrix:
            ciphertext.append(row[col_idx])
    
    return ''.join(ciphertext)

def generate_key() -> str:
    """Generate a random keyword for columnar transposition."""
    keywords = ['KEY', 'CODE', 'CIPHER', 'SECRET', 'CRYPTO', 'ALPHA', 'BETA']
    return random.choice(keywords)

def process_text(text: str) -> str:
    """
    Process text using Columnar Transposition Encryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        key = generate_key()
        ciphertext = encrypt_columnar(text, key)
        result = f"Ciphertext: {ciphertext}\n\nKey (Keyword): {key}"
        return result
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

