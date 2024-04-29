from sympy import randprime
from sympy import mod_inverse
import random
import math

# Choose two distinct primes each consisting of at least three digits
p = randprime(100, 999)
q = randprime(1000, 9999)

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and e is co-prime with n and phi
def find_e(phi):
    while True:
        e = random.randrange(2, phi)
        if math.gcd(e, phi) == 1:
            return e

e = find_e(phi)

# Calculate d such that (d * e) % phi = 1
d = mod_inverse(e, phi)

print(f"RSA Model:")
print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")

# Diffie-Hellman Key Exchange
g = p  # Let's use the bigger prime as the base
alice_private = random.randint(5, 10)  # A random private key for Alice
bob_private = random.randint(10, 20)  # A random private key for Bob

alice_public = g ** alice_private
bob_public = g ** bob_private

alice_secret = bob_public ** alice_private
bob_secret = alice_public ** bob_private

print("\nDiffie-Hellman Key Exchange:")
print(f"Alice's public key: {alice_public}")
print(f"Bob's public key: {bob_public}")
print(f"Alice's secret key: {alice_secret}")
print(f"Bob's secret key: {bob_secret}")
