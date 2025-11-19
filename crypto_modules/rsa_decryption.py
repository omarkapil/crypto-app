from .rsa_encryption import build_keys
from .utils import DEFAULT_SEED


def decrypt(numbers: list[int], n: int, d: int) -> str:
    chars = [chr(pow(num, d, n)) for num in numbers]
    return "".join(chars)


def parse_numbers(text: str) -> list[int]:
    try:
        return [int(part) for part in text.strip().split()]
    except ValueError as exc:
        raise ValueError("Ciphertext must be space-separated integers.") from exc


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    try:
        numbers = parse_numbers(text)
    except ValueError as exc:
        return f"ERROR: {exc}"

    n, _, d, seed = build_keys(DEFAULT_SEED)
    plain = decrypt(numbers, n, d)
    return (
        f"Plaintext: {plain}\n"
        f"Private Key (n, d): ({n}, {d})\n"
        f"Seed: {seed}"
    )

