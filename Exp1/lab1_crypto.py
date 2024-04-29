from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import copy

def sub_bytes(state):
    # Substitute bytes using a fixed S-box
    for i in range(4):
        for j in range(4):
            state[i][j] = s_box[state[i][j]]
    return state

def shift_rows(state):
    # Shift rows as per AES
    return [row[i:] + row[:i] for i, row in enumerate(state)]

def shift_columns(state):
    # Shift columns as per custom requirement
    return [row[-i:] + row[:-i] for i, row in enumerate(state)]

def xor_key(state, round_key):
    # XOR state with round key
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    return state

def key_schedule(key):
    # Generate round keys from the initial key
    round_keys = [key]
    for round_num in range(1, 11):
        prev_key = copy.deepcopy(round_keys[-1])
        # Shift rows and substitute bytes for the new round key
        new_key = sub_bytes(shift_rows(prev_key))
        round_keys.append(new_key)
    return round_keys

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), AES.block_size))

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

# Main program
s_box = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    # ... (complete S-box here)
]

# Example plaintext and key
plaintext = "Hello, AES!"
initial_key = get_random_bytes(16)

# Encryption
round_keys = key_schedule(initial_key)
state = [[ord(char) for char in block] for block in plaintext[:16]]
for round_key in round_keys:
    state = sub_bytes(state)
    state = shift_rows(state)
    state = shift_columns(state)
    state = xor_key(state, round_key)

# Output ciphertext
ciphertext = bytes([char for block in state for char in block])
print(f"Ciphertext: {ciphertext.hex()}")

# Decryption
state = [[char for char in block] for block in ciphertext]
for round_key in reversed(round_keys):
    state = xor_key(state, round_key)
    state = shift_columns(state)
    state = shift_rows(state)
    state = sub_bytes(state)

# Output decrypted plaintext
decrypted_plaintext = ''.join([chr(char) for block in state for char in block])
print(f"Decrypted Plaintext: {decrypted_plaintext}")

# Verify if the decrypted plaintext matches the original
if decrypted_plaintext == plaintext:
    print("Verification: Matched")
else:
    print("Verification: Not Matched")
