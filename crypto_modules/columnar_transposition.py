# Columnar Transposition Cipher
# A transposition cipher that rearranges columns based on a keyword

import math

def encrypt_columnar(text: str, key: str) -> str:
    """Encrypt text using columnar transposition cipher."""
    # Remove spaces and convert to uppercase
    text = text.replace(' ', '').upper()
    key = key.upper()
    
    # Create matrix
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    
    # Pad text if necessary
    text += 'X' * (num_cols * num_rows - len(text))
    
    # Create matrix
    matrix = [list(text[i:i+num_cols]) for i in range(0, len(text), num_cols)]
    
    # Get sorted key indices
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    key_order = [x[0] for x in sorted_key]
    
    # Read columns in key order
    ciphertext = []
    for col_idx in key_order:
        for row in matrix:
            ciphertext.append(row[col_idx])
    
    return ''.join(ciphertext)

def decrypt_columnar(ciphertext: str, key: str) -> str:
    """Decrypt text using columnar transposition cipher."""
    key = key.upper()
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    
    # Get sorted key indices
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    key_order = [x[0] for x in sorted_key]
    
    # Create inverse mapping
    inverse_order = [0] * num_cols
    for i, col_idx in enumerate(key_order):
        inverse_order[col_idx] = i
    
    # Reconstruct matrix
    matrix = [[''] * num_cols for _ in range(num_rows)]
    char_idx = 0
    
    for col_idx in key_order:
        for row_idx in range(num_rows):
            if char_idx < len(ciphertext):
                matrix[row_idx][col_idx] = ciphertext[char_idx]
                char_idx += 1
    
    # Read row by row
    plaintext = ''.join([''.join(row) for row in matrix])
    return plaintext.rstrip('X')

def generate_key() -> str:
    """Generate a random keyword for columnar transposition."""
    import random
    keywords = ['KEY', 'CODE', 'CIPHER', 'SECRET', 'CRYPTO', 'ALPHA', 'BETA']
    return random.choice(keywords)

def process_text(text: str) -> str:
    """
    Process text using Columnar Transposition Cipher for Flask app.
    Encrypts the text using a random keyword.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        # Generate a random key
        key = generate_key()
        
        # Encrypt
        ciphertext = encrypt_columnar(text, key)
        
        result = f"Ciphertext: {ciphertext}\n\nKey (Keyword): {key}"
        return result
        
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

