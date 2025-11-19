# Simple CBC Encryption (XOR-based)
from .utils import DEFAULT_SEED, generate_lcg_bytes

BLOCK_SIZE = 8


def pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    if pad_len == 0:
        pad_len = BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt_blocks(data: bytes, key: bytes, iv: bytes) -> bytes:
    ciphertext = bytearray()
    previous = iv
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i + BLOCK_SIZE]
        mixed = xor_bytes(block, previous)
        cipher_block = xor_bytes(mixed, key)
        ciphertext.extend(cipher_block)
        previous = cipher_block
    return bytes(ciphertext)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = generate_lcg_bytes(DEFAULT_SEED, BLOCK_SIZE)
    iv = generate_lcg_bytes(DEFAULT_SEED + 1, BLOCK_SIZE)
    padded = pad(text.encode("utf-8"))
    cipher = encrypt_blocks(padded, key, iv)
    return (
        f"Ciphertext (hex): {cipher.hex()}\n"
        f"Key (hex): {key.hex()}\n"
        f"IV (hex): {iv.hex()}\n"
        f"Seed: {DEFAULT_SEED}"
    )

