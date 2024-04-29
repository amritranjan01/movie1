import random

# Helper function to find the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Helper function to find modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Helper function to generate random prime number
def generate_prime(lower, upper):
    while True:
        num = random.randint(lower, upper)
        if is_prime(num):
            return num

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Choose two distinct primes each consisting of at least three digits
p = generate_prime(100, 999)
q = generate_prime(1000, 9999)

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and e is co-prime with n and phi
def find_e(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e

e = find_e(phi)

# Calculate d such that (d * e) % phi = 1
d = mod_inverse(e, phi)

print("RSA Model:")
print("Public key:", (e, n))
print("Private key:", (d, n))

# Diffie-Hellman Key Exchange
g = p  # Let's use the bigger prime as the base
alice_private = random.randint(5, 10)  # A random private key for Alice
bob_private = random.randint(10, 20)  # A random private key for Bob

alice_public = pow(g, alice_private)
bob_public = pow(g, bob_private)

alice_secret = pow(bob_public, alice_private)
bob_secret = pow(alice_public, bob_private)

print("\nDiffie-Hellman Key Exchange:")
print("Alice's public key:", alice_public)
print("Bob's public key:", bob_public)
print("Alice's secret key:", alice_secret)
print("Bob's secret key:", bob_secret)
