# This script performs a basic affine cipher.

inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
a = 4
b = 16
modulo = 26
encrypt = -1 # change to -1 to decrypt

if encrypt == -1:
    for x in range(modulo):
        if ((a * x) % modulo) == 1:
            a = x
            break
    print(a)

outputtext = ""
for char in inputtext.lower():
    if char.isalpha():
        if encrypt == 1:
            outputtext += chr(((((ord(char) - 97) * a) + b) % modulo) + 97)
        else:
            outputtext += chr(((((ord(char) - 97) - b) * a) % modulo) + 97)

print(outputtext)
