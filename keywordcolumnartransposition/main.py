# This code performs a columnar transposition from a number
import math

def unique(messychars):
    uniquechars = ""
    for x in messychars:
        if x not in uniquechars:
            uniquechars += x
    return uniquechars


inputtext = "ATYOSOPMWRKMNACRHEEPTGILAEOEFDEOTHCNOOHN"
keyword = "beark"
encrypt = -1 # change to -1 to decrypt

inputtext = inputtext.replace(" ", "")
alphabet = "abcdefghijklmnopqrstuvwxyz"

key = [0] * len(unique(keyword))
i = 0
j = 0
for char in unique(keyword):
    key[i] = alphabet.find(char)
    i += 1
temp = key.copy()
temp.sort()
for i in temp:
    key[key.index(i)] = j
    j += 1
temp = key.copy()
temp.sort()
outputtext = ""
if encrypt == 1:
    for i in temp:
        i = key.index(i)
        for j in range(i, len(inputtext), len(key)):
            print(i, j)
            outputtext += inputtext[j]
else:
    for i in range(math.ceil(len(inputtext) / len(key))):
        for j in key:
            outputtext += inputtext[math.ceil(len(inputtext) / len(key)) * j + i]

print(outputtext)

