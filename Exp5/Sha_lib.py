import hashlib
import random

# Generate a binary string of length 1000
binary_string = ''.join(random.choice('01') for _ in range(1000))

# Convert binary string to bytes
binary_bytes = int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, 'big')

# Apply SHA-256 hash function
hash_object = hashlib.sha256(binary_bytes)

# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

print(f"Binary String: {binary_string}")
print(f"SHA-256 Hash: {hex_dig}")
