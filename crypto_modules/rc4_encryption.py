# RC4 Encryption
# ملف التشفير بتقنية RC4

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

def rc4_lcg_encrypt(plaintext, key):
    key_bytes = [ord(c) for c in key]
    S = ksa(key_bytes)
    seed = sum(S) % 256
    keystream = lcg_keystream(len(plaintext), seed)
    ciphertext_bytes = xor_cipher(plaintext, keystream)
    return base64.b64encode(ciphertext_bytes).decode('ascii')

def process_text(text: str, key: str = "defaultkey") -> str:
    """
    Process text using RC4 Encryption.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        data_bytes = text.encode('utf-8')
        ciphertext_b64 = rc4_lcg_encrypt(data_bytes, key)
        result = f"Ciphertext (Base64): {ciphertext_b64}\n\nKey: {key}"
        return result
    except Exception as e:
        return f"ERROR: Encryption failed: {str(e)}"

