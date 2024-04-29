import hashlib

# Example usage:
message = b"Hello, this is a test message for MD5 hashing!"

# Using hashlib library for MD5 hashing
md5_hash = hashlib.md5(message).hexdigest()
print("Original Message: ",message)
print("MD5 Hash (using hashlib):", md5_hash)
