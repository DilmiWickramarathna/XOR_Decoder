def xor_decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using the XOR operation with the provided key.
    :param ciphertext: The encrypted data as a byte array.
    :param key: The key as a byte array.
    :return: The decrypted plaintext as a byte array.
    """
    key_length = len(key)
    decrypted = bytearray(len(ciphertext))
    for i in range(len(ciphertext)):
        decrypted[i] = ciphertext[i] ^ key[i % key_length]
    return decrypted

# Load the encrypted file
input_file = 'encoded.enc'  # Replace with your .enc file path

# Known plaintext
known_plaintext = b"Hello, You ha"

with open(input_file, 'rb') as f:
    encrypted_data = f.read()

# Extract the key using the known plaintext
key_length = 120 // 8  # 120 bits = 15 bytes
key = bytearray(key_length)
for i in range(len(known_plaintext)):
    key[i % key_length] = encrypted_data[i] ^ known_plaintext[i]

with open("output.txt", "wb") as file:
    for i in range (0,128):
        for j in range (0,128):
            binary_value1 = bin(i)
            binary_value2 = bin(j)
            ascii_value1 = chr(int(binary_value1, 2))
            ascii_value2 = chr(int(binary_value2, 2))
            key.pop()
            key.pop()
            key.append(ord(ascii_value1))
            key.append(ord(ascii_value2))
            plaintext = xor_decrypt(encrypted_data, key)
            file.write(plaintext)
            file.write(b"\n")
            file.write(key)
            file.write(b"\n")
            file.write(b"##################################################################################################################################################")
            file.write(b"\n")
