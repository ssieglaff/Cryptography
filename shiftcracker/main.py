# This script attempts to crack a shift cipher via frequency analysis

plaintext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
plaintext = plaintext.lower()

alphabet = [0] * 26
for x in plaintext:
    if x.isalpha():
        alphabet[ord(x.lower()) - 97] += 1

print()
print("v most likely v")
print("key: message")
for i in range(len(alphabet)):
    highest = 0
    for x in range(len(alphabet)):
        if alphabet[highest] <= alphabet[x]:
            highest = x
    key = (highest - 4) % 26
    alphabet[highest] = -1

    letters = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    for x in plaintext:
        if x.isalpha():
            ciphertext += letters[(letters.find(x) - key) % 26]
        else:
            ciphertext += x
    printval = " {0:>2n}: {1}"
    print(printval.format(key, ciphertext))
print("^ least likely ^")
