# Monoalphabetic Cipher (Substitution Cipher)
# Simple substitution cipher where each letter is replaced with another letter

import random
import string

def generate_key():
    """Generate a random monoalphabetic substitution key."""
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def encrypt(text: str, key: dict) -> str:
    """Encrypt text using monoalphabetic cipher."""
    result = []
    for char in text.upper():
        if char in key:
            result.append(key[char])
        elif char.isalpha():
            # Handle lowercase by converting
            result.append(key[char.upper()].lower())
        else:
            result.append(char)
    return ''.join(result)

def decrypt(text: str, key: dict) -> str:
    """Decrypt text using monoalphabetic cipher."""
    reverse_key = {v: k for k, v in key.items()}
    result = []
    for char in text:
        if char.upper() in reverse_key:
            if char.isupper():
                result.append(reverse_key[char])
            else:
                result.append(reverse_key[char.upper()].lower())
        else:
            result.append(char)
    return ''.join(result)

def process_text(text: str) -> str:
    """
    Process text using Monoalphabetic Cipher for Flask app.
    Encrypts the text and returns the ciphertext with the key.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        # Generate a random key
        key = generate_key()
        
        # Encrypt the text
        ciphertext = encrypt(text, key)
        
        # Format key for display
        key_str = " ".join([f"{k}->{v}" for k, v in sorted(key.items())])
        
        result = f"Ciphertext: {ciphertext}\n\nKey (A->Z mapping):\n{key_str}"
        return result
        
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

