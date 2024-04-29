import random
import hashlib

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Fast modular exponentiation
def fast_power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# ElGamal key generation
def generate_keys(p, g):
    x = random.randint(2, p - 2)
    y = fast_power(g, x, p)
    return x, y

# ElGamal digital signature
def sign(message, p, g, x):
    # Generate k such that 1 < k < p-1 and gcd(k, p-1) = 1
    k = random.randint(2, p - 2)
    while extended_gcd(k, p - 1)[0] != 1:
        k = random.randint(2, p - 2)

    r = fast_power(g, k, p)
    h = int(hashlib.sha1(message.encode()).hexdigest(), 16)
    s = (mod_inverse(k, p - 1) * (h - x * r)) % (p - 1)
    return (r, s)

# ElGamal signature verification
def verify(message, signature, p, g, y):
    r, s = signature
    if not (0 < r < p and 0 < s < p - 1):
        return False

    h = int(hashlib.sha1(message.encode()).hexdigest(), 16)
    left = fast_power(y, r, p) * fast_power(r, s, p) % p
    right = fast_power(g, h, p)
    return left == right

# Example usage
if __name__ == "__main__":
    # Parameters
    p = 101
    g = 2

    # Generate keys
    x, y = generate_keys(p, g)

    # Message to be signed
    message = "Hello, World!"

    # Sign the message
    signature = sign(message, p, g, x)
    print("Signature:", signature)

    # Verify the signature
    is_verified = verify(message, signature, p, g, y)
    if is_verified:
        print("Signature is verified.")
    else:
        print("Signature verification failed.")
