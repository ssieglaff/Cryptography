# This code performs a columnar transposition from a number
import math

inputtext = "ATYOSOPMWRKMNACRHEEPTGILAEOEFDEOTHCNOOHN"
columns = 15
encrypt = -1 # change to -1 to decrypt

inputtext = inputtext.replace(" ", "")
alphabet = "abcdefghijklmnopqrstuvwxyz"
outputtext = ""
if encrypt == 1:
    for i in range(columns):
        for j in range(i, len(inputtext), columns):
            outputtext += inputtext[j]
else:
    for i in range(math.ceil(len(inputtext) / columns)):
        for j in range(i, len(inputtext), math.ceil(len(inputtext) / columns)):
            outputtext += inputtext[j]

print(outputtext)

