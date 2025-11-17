# SHA-1 Hashing
# ملف الهاشينج بتقنية SHA-1

def leftRotate(value, count):
    return ((value << count) | (value >> (32 - count))) & 0xFFFFFFFF

def sha1(input):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    message = bytearray(input.encode('utf-8'))
    message.append(0x80)

    while (len(message) * 8) % 512 != 448:
        message.append(0x00)

    originalBitLen = len(input) * 8
    for i in range(7, -1, -1):
        message.append((originalBitLen >> (i * 8)) & 0xFF)

    for chunk in range(0, len(message), 64):
        w = [0] * 80

        for i in range(16):
            base = chunk + i * 4
            w[i] = (message[base + 0] << 24) \
                 | (message[base + 1] << 16) \
                 | (message[base + 2] << 8) \
                 | message[base + 3]

        for i in range(16, 80):
            w[i] = leftRotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (leftRotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF

            e = d
            d = c
            c = leftRotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

def process_text(text: str) -> str:
    """
    Process text using SHA-1 Hashing.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        hash_result = sha1(text)
        result = f"SHA-1 Hash: {hash_result}\n\nMessage: {text}"
        return result
    except Exception as e:
        return f"ERROR: Hashing failed: {str(e)}"

