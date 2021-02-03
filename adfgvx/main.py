# This is code to implement the ADFGVX cipher.

plaintext = "armymoves6december"
keyword = "berlin"

adfgvx = "adfgvx"
table = "fl1ao2jdw3guciyb4pr5q8ve6k7zmxsnh0t9"
alphabet = "abcdefghijklmnopqrstuvwxyz"
substitution = ""
ciphertext = ""

for x in plaintext:
    i = table.find(x)
    a = i // 6
    b = i % 6
    key = adfgvx[a] + adfgvx[b]
    substitution += key

for x in alphabet:
    i = keyword.find(x)
    if i != -1:
        for j in range(i, len(substitution), len(keyword)):
            ciphertext += substitution[j]

print(ciphertext)