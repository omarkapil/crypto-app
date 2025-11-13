# RSA 

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    """Find modular inverse of a mod m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keys():
    # Use larger primes so n > max(ord(char))
    p = 17
    q = 19
    n = p * q  # n = 323
    phi = (p - 1) * (q - 1)

    e = 5  # public key exponent
    d = modinv(e, phi)  # private key exponent

    return (e, n), (d, n)

def encrypt(message, pub_key):
    """Encrypt a text message to a list of numbers"""
    e, n = pub_key
    return [(ord(c) ** e) % n for c in message]

def decrypt(cipher, priv_key):
    """Decrypt a list of numbers back to text"""
    d, n = priv_key
    return ''.join([chr((num ** d) % n) for num in cipher])

# ----- MAIN PROGRAM -----
print("=== RSA Transparent Encryption ===")

public_key, private_key = generate_keys()

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()

if choice == 'e':
    message = input("Enter your message: ")
    encrypted_msg = encrypt(message, public_key)
    print("\nEncrypted message:", encrypted_msg)
    print("Give these numbers to the other user to decrypt the message.\n")

elif choice == 'd':
    cipher_input = input("Enter encrypted numbers separated by spaces: ")
    try:
        cipher = [int(x) for x in cipher_input.split()]
        decrypted_msg = decrypt(cipher, private_key)
        print("\nDecrypted message:", decrypted_msg)
    except ValueError:
        print("Error: Please enter numbers only.")

else:
    print("Invalid choice. Choose E or D.")