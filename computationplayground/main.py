# General code space to perform random computations
import re

# encode letter pairs as decimal base 26 value
#inputtext = "helloworld"
#
#inputtext = re.compile('[^a-z]').sub('', inputtext.lower())
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#for a in range(0, len(inputtext), 2):
#    print(alphabet.find(inputtext[a]) * 25 + alphabet.find(inputtext[a + 1]))
test = (11415678 << 128) + (11415678 << 64) + 11415678
print(test)
