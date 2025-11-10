# RC4 (Rivest Cipher 4)
# Stream cipher algorithm

import os
import base64

def KSA(key: bytes) -> list:
    """Key Scheduling Algorithm - Initialize the S array."""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S: list, n: int) -> list:
    """Pseudo-Random Generation Algorithm - Generate keystream."""
    i = 0
    j = 0
    keystream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream

def rc4_encrypt(plaintext: bytes, key: bytes) -> bytes:
    """Encrypt plaintext using RC4."""
    S = KSA(key)
    keystream = PRGA(S, len(plaintext))
    ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
    return ciphertext

def rc4_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    """Decrypt ciphertext using RC4 (same as encryption)."""
    return rc4_encrypt(ciphertext, key)

def process_text(text: str) -> str:
    """
    Process text using RC4 encryption for Flask app.
    Encrypts the text and returns base64 encoded ciphertext with key.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        # Generate a random 16-byte key
        key = os.urandom(16)
        
        # Encrypt
        plaintext_bytes = text.encode('utf-8')
        ciphertext = rc4_encrypt(plaintext_bytes, key)
        
        # Encode in base64 for display
        ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')
        key_b64 = base64.b64encode(key).decode('utf-8')
        
        result = f"Ciphertext (base64): {ciphertext_b64}\n\nKey (base64): {key_b64}"
        return result
        
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

