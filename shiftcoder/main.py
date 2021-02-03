# This is code to implement shift cipher encryption and decryption

plaintext = "bzcm ewzbp qa qv jmqvo vwb ammuqvo"
key = 2 # Number of letters to shift
encrypt = -1 # Change to -1 to decrypt

alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""

for x in plaintext:
    if x.isalpha():
        ciphertext += alphabet[(alphabet.find(x) + (encrypt * key)) % 26]
    else:
        ciphertext += x
print(ciphertext)
