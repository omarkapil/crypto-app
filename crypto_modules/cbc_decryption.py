# CBC Decryption (matching the simple XOR-based encryption)
from .utils import DEFAULT_SEED, generate_lcg_bytes
from .cbc_encryption import BLOCK_SIZE, xor_bytes


def unpad(data: bytes) -> bytes:
    if not data:
        return b""
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        return data
    return data[:-pad_len]


def decrypt_blocks(data: bytes, key: bytes, iv: bytes) -> bytes:
    plaintext = bytearray()
    previous = iv
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i + BLOCK_SIZE]
        mixed = xor_bytes(block, key)
        plain_block = xor_bytes(mixed, previous)
        plaintext.extend(plain_block)
        previous = block
    return bytes(plaintext)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is required (hex)."

    try:
        cipher = bytes.fromhex(text.strip())
    except ValueError:
        return "ERROR: Ciphertext must be hex encoded."

    key = generate_lcg_bytes(DEFAULT_SEED, BLOCK_SIZE)
    iv = generate_lcg_bytes(DEFAULT_SEED + 1, BLOCK_SIZE)
    plain_padded = decrypt_blocks(cipher, key, iv)
    plain = unpad(plain_padded)

    try:
        decoded = plain.decode("utf-8")
    except UnicodeDecodeError:
        decoded = plain.decode("latin-1")

    return (
        f"Plaintext: {decoded}\n"
        f"Key (hex): {key.hex()}\n"
        f"IV (hex): {iv.hex()}\n"
        f"Seed: {DEFAULT_SEED}"
    )

