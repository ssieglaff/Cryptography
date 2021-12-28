# This is python code to compute the Vigenere cypher.
import re

inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
key = ""
encrypt = -1 # 1 to encrypt, -1 to decrypt


alphabet = "abcdefghijklmnopqrstuvwxyz"
outputtext = ""
inputtext = re.compile('[^a-z]').sub('', inputtext.lower())
for i in range(len(inputtext)):
    outputtext += alphabet[(alphabet.find(inputtext[i]) + encrypt * alphabet.find(key[i % len(key)])) % len(alphabet)]
print(outputtext)
