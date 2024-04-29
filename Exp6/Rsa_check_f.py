from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate keys for Entity A (sender)
key_A = RSA.generate(2048)
private_key_A = key_A.export_key()
public_key_A = key_A.publickey().export_key()

# Generate keys for Entity B (receiver)
key_B = RSA.generate(2048)
private_key_B = key_B.export_key()
public_key_B = key_B.publickey().export_key()

# Entity A signs a message
def sign_message(message, private_key):
    hash_value = SHA256.new(message.encode())
    signer = pkcs1_15.new(RSA.import_key(private_key))
    signature = signer.sign(hash_value)
    return signature

# Entity B verifies the signature
def verify_signature(message, signature, public_key):
    hash_value = SHA256.new(message.encode())
    verifier = pkcs1_15.new(RSA.import_key(public_key))
    try:
        pkcs1_15.new(RSA.import_key(public_key)).verify(hash_value, signature)
        return True
    except (ValueError, TypeError):
        return False

# Entity A encrypts a message for Entity B
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher.encrypt(message.encode())
    return base64.b64encode(ciphertext).decode()

# Entity B decrypts the message from Entity A
def decrypt_message(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    ciphertext = base64.b64decode(ciphertext)
    decrypted_message = cipher.decrypt(ciphertext).decode()
    return decrypted_message

# Example usage
message = "Hello, Entity B!"

# Entity A signs and encrypts the message
signature = sign_message(message, private_key_A)
encrypted_message = encrypt_message(message, public_key_B)

# Entity B verifies the signature and decrypts the message
is_signature_valid = verify_signature(message, signature, public_key_A)
decrypted_message = decrypt_message(encrypted_message, private_key_B)

# Display results
print(f"Signature verification: {is_signature_valid}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
