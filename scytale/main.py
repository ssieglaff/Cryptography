# This code is to decipher a simple version of the Spartan Scytale cipher.

plaintext = "ATYOSOPMWRKMNACRHEEPTGILAEOEFDEOTHCNOOHN"
# the number of lines the message was written in
line = 8
ciphertext = ""
for i in range(line - 1):
    for j in range(i, len(plaintext), line):
        ciphertext += plaintext[j]
print(ciphertext)
