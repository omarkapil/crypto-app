# Hill Cipher - Encryption
# ملف التشفير بتقنية Hill Cipher

import numpy as np

def text_to_numbers(text: str) -> list:
    """Convert text to numbers (A=0, B=1, ..., Z=25)."""
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

def numbers_to_text(numbers: list) -> str:
    """Convert numbers to text (0=A, 1=B, ..., 25=Z)."""
    return ''.join([chr(n + ord('A')) for n in numbers])

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def generate_key_matrix(size: int = 2):
    """Generate a random invertible key matrix for Hill cipher."""
    import math
    max_attempts = 1000
    for _ in range(max_attempts):
        matrix = np.random.randint(0, 26, size=(size, size))
        det = int(np.round(np.linalg.det(matrix))) % 26
        if det != 0 and gcd(abs(det), 26) == 1:
            return matrix
    return np.array([[3, 3], [2, 5]])

def encrypt_hill(plaintext: str, key_matrix: np.ndarray) -> str:
    """Encrypt text using Hill cipher."""
    numbers = text_to_numbers(plaintext)
    n = len(key_matrix)
    
    while len(numbers) % n != 0:
        numbers.append(0)
    
    ciphertext_numbers = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext_numbers.extend(encrypted_block.tolist())
    
    return numbers_to_text(ciphertext_numbers)

def process_text(text: str) -> str:
    """
    Process text using Hill Cipher Encryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        clean_text = ''.join([c for c in text if c.isalpha()])
        if not clean_text:
            return "ERROR: Text must contain at least one letter."
        
        key_matrix = generate_key_matrix(2)
        ciphertext = encrypt_hill(clean_text, key_matrix)
        
        key_str = f"Key Matrix (2x2):\n{key_matrix[0]}\n{key_matrix[1]}"
        result = f"Ciphertext: {ciphertext}\n\n{key_str}"
        return result
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

