# RC4 Decryption
# ملف فك التشفير بتقنية RC4

import base64

def ksa(key_bytes):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def lcg_keystream(length, seed, a=1103515245, c=12345, m=256):
    stream = bytearray()
    x = seed
    for _ in range(length):
        x = (a * x + c) % m
        stream.append(x)
    return bytes(stream)

def xor_cipher(data_bytes, keystream):
    return bytes(b ^ k for b, k in zip(data_bytes, keystream))

def rc4_lcg_decrypt(ciphertext_b64, key):
    try:
        ciphertext_bytes = base64.b64decode(ciphertext_b64)
    except Exception:
        raise ValueError("Invalid Base64 encoding.")
    
    key_bytes = [ord(c) for c in key]
    S = ksa(key_bytes)
    seed = sum(S) % 256
    keystream = lcg_keystream(len(ciphertext_bytes), seed)
    decrypted_bytes = xor_cipher(ciphertext_bytes, keystream)
    
    try:
        return decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return f"[Binary Data: {decrypted_bytes.hex()}]"

def process_text(text: str, key: str = "defaultkey") -> str:
    """
    Process text using RC4 Decryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        plaintext = rc4_lcg_decrypt(text, key)
        result = f"Plaintext: {plaintext}\n\nKey: {key}"
        return result
    except ValueError as e:
        return f"ERROR: {str(e)}"
    except Exception as e:
        return f"ERROR: Decryption failed: {str(e)}"

