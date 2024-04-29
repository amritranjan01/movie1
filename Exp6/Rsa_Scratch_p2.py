import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def generate_keypair(bits):
    # Step 1: Choose two large prime numbers, p and q
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    # Step 2: Compute n = pq and Euler's totient function phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = random.randrange(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)

    # Step 4: Compute d, the modular multiplicative inverse of e (mod phi_n)
    d = mod_inverse(e, phi_n)

    return ((n, e), (n, d))

def generate_prime(bits):
    candidate = random.getrandbits(bits)
    while not is_prime(candidate):
        candidate = random.getrandbits(bits)
    return candidate

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # n is composite
    return True  # n is probably prime

def sign_message(message, private_key):
    n, d = private_key
    signature = [mod_exp(ord(char), d, n) for char in message]
    return signature

def verify_signature(message, signature, public_key):
    n, e = public_key
    expected_message = ''.join([chr(mod_exp(char, e, n)) for char in signature])
    return message == expected_message

def encrypt_message(message, public_key):
    n, e = public_key
    cipher_text = [mod_exp(ord(char), e, n) for char in message]
    return cipher_text

def decrypt_message(cipher_text, private_key):
    n, d = private_key
    plain_text = ''.join([chr(mod_exp(char, d, n)) for char in cipher_text])
    return plain_text

# Example usage
message = "Hello, Entity B!"
public_key_A, private_key_A = generate_keypair(256)
public_key_B, private_key_B = generate_keypair(256)

# Entity A signs and encrypts the message
signature_A = sign_message(message, private_key_A)
encrypted_message = encrypt_message(message, public_key_B)

# Entity B verifies the signature and decrypts the message
is_signature_valid = verify_signature(message, signature_A, public_key_A)
decrypted_message = decrypt_message(encrypted_message, private_key_B)

# Display results
print(f"Original message: {message}")
print(f"Signature verification: {is_signature_valid}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
