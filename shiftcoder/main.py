# This is code to implement shift cipher encryption and decryption

plaintext = "Cryptography"
key = 13 # Number of letters to shift
encrypt = -1 # Change to -1 to decrypt

alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""
plaintext = plaintext.lower()
for x in plaintext:
    if x.isalpha():
        ciphertext += alphabet[(alphabet.find(x) + (encrypt * key)) % 26]
    else:
        ciphertext += x
print(ciphertext)
