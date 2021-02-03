# This is python code to compute the Vigenere cypher.

plaintext = "walterraleighbringstobaccotoenglandfromamerica"
primingkey = "b"
# change to -1 to decrypt
encrypt = 1


alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""
i = 0
if encrypt == 1:
    key = primingkey + plaintext
    for x in range(len(plaintext)):
        pt = alphabet.find(plaintext[x])
        ky = alphabet.find(key[x])
        ciphertext += alphabet[(pt + ky) % 26]
        i += 1
else:
    key = primingkey
    for x in range(len(plaintext)):
        a = alphabet.find(plaintext[x])
        b = alphabet.find(key[x])
        c = alphabet[(a - b) % 26]
        ciphertext += c
        key += c
        i += 1
print(ciphertext)
