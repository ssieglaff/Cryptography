# This code performs a substitution cipher based on a columnar transposition alphabet

def unique(messychars):
    uniquechars = ""
    for x in messychars:
        if x not in uniquechars:
            uniquechars += x
    return uniquechars


inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
key = "geodsic"
encrypt = -1 # change to -1 to decrypt

columns = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipheralphabet = ""
outputtext = ""
inputtext = inputtext.lower()
for char in unique(key):
    if char.isalpha():
        cipheralphabet += char
        columns += 1
cipheralphabet += alphabet
cipheralphabet = unique(cipheralphabet)
temp = ""
for i in range(columns):
    for j in range(i, len(cipheralphabet), columns):
        temp += cipheralphabet[j]
cipheralphabet = temp
print(cipheralphabet)
for char in inputtext:
    if char.isalpha():
        if encrypt == 1:
            outputtext += cipheralphabet[alphabet.find(char)]
        else:
            outputtext += alphabet[cipheralphabet.find(char)]
print(outputtext)
