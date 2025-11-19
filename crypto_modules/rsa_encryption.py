from .utils import DEFAULT_SEED, generate_lcg_prime_pair


def mod_inverse(a: int, m: int) -> int:
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse found.")


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def build_keys(seed: int) -> tuple[int, int, int, int]:
    p, q = generate_lcg_prime_pair(seed)
    n = p * q
    phi = (p - 1) * (q - 1)
    for candidate in (65537, 257, 17, 5, 3):
        if gcd(candidate, phi) == 1:
            e = candidate
            break
    else:
        e = 3
    d = mod_inverse(e, phi)
    return n, e, d, seed


def encrypt(text: str, n: int, e: int) -> list[int]:
    values: list[int] = []
    for char in text:
        values.append(pow(ord(char), e, n))
    return values


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    n, e, _, seed = build_keys(DEFAULT_SEED)
    cipher_numbers = encrypt(text, n, e)
    cipher_str = " ".join(str(num) for num in cipher_numbers)
    return (
        f"Ciphertext: {cipher_str}\n"
        f"Public Key (n, e): ({n}, {e})\n"
        f"Seed: {seed}"
    )

