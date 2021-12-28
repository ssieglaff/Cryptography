import re
import itertools

inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
keysize = 5 # suspected key length to brute force


alphabet = "abcdefghijklmnopqrstuvwxyz"
outputtext = ""
inputtext = re.compile('[^a-z]').sub('', inputtext.lower())
for key in itertools.product(alphabet, repeat=keysize):
    for i in range(len(inputtext)):
        outputtext += alphabet[(alphabet.find(inputtext[i]) - alphabet.find(key[i % len(key)])) % len(alphabet)]
    if "the" in outputtext:
        print(outputtext)
    outputtext = ""
