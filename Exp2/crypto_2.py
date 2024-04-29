def bits_to_int(bits):
    return int(''.join(map(str, bits)), 2)

def int_to_bits(n, num_bits):
    return [int(bit) for bit in format(n, '0' + str(num_bits) + 'b')]

def cyclic_left_shift(bits):
    return bits[1:] + bits[:1]

def cyclic_right_shift(bits):
    return bits[-1:] + bits[:-1]

def sbox(bits):
    sbox = [0, 0xf, 1, 0xe, 2, 0xd, 3, 0xc, 4, 0xb, 5, 0xa, 6, 9, 7, 8]
    return int_to_bits(sbox[bits_to_int(bits)], 4)

def inverse_sbox(bits):
    inverse_sbox = [0, 2, 4, 8, 3, 10, 12, 14, 15, 13, 5, 9, 7, 1, 11, 6]
    return int_to_bits(inverse_sbox[bits_to_int(bits)], 4)

def permutation(bits):
    perm = [0, 2, 4, 6, 1, 3, 5, 7]
    return [bits[i] for i in perm]

def inverse_permutation(bits):
    inverse_perm = [0, 4, 1, 5, 2, 6, 3, 7]
    return [bits[i] for i in inverse_perm]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def encrypt(plain_text, key):
    L, R = plain_text[:4], plain_text[4:]
    L, R = cyclic_left_shift(L), cyclic_left_shift(R)
    L, R = sbox(L), sbox(R)
    bits = permutation(L + R)
    cipher_text = xor(bits, key)
    return cipher_text

def decrypt(cipher_text, key):
    bits = xor(cipher_text, key)
    L, R = inverse_permutation(bits)[:4], inverse_permutation(bits)[4:]
    L, R = inverse_sbox(L), inverse_sbox(R)
    plain_text = cyclic_right_shift(L) + cyclic_right_shift(R)
    return plain_text

# Test the encryption and decryption
plain_text = [1, 0, 1, 0, 1, 1, 0, 1]
key = [0, 1, 0, 1, 1, 0, 1, 0]

cipher_text = encrypt(plain_text, key)
print("Cipher Text: ", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted Text: ", decrypted_text)

assert plain_text == decrypted_text, "Decryption did not match the original plain text!"
