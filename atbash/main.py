# This is python code to compute the atbash cypher of a string.

plaintext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""
i = 0
for x in plaintext.lower():
    j = alphabet.find(x)
    if j >= 0:
        ciphertext += alphabet[25 - j]
    else:
        ciphertext += x
    i += 1
print(ciphertext)
