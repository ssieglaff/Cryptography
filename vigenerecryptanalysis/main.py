# This code is designed to deduce a keyword from a vigenere ciphertext using a the signature and scrawl
# analysis technique discussed in chapter 2.8 of the book "Invitation to Cryptology" by Thomas Barr.
import re

inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
probkey = 5 # leave 0 to analyze for key length, otherwise change to suspected length
maxkey = 10 # the longest key you think is possible (only matters if analyzing for key length)

inputtext = re.compile('[^a-z]').sub('', inputtext.lower())

# tests key sizes up to a length of maxkey
if probkey == 0:
    print("Computing likely key lengths: ")
    maxdiff, probkey = 0, 0
    Avals = [0] * maxkey
    for l in range(1, maxkey + 1):
        # count frequency for each coset
        avgcosetdiff = 0
        for coset in range(0, l):
            alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
            total = 0
            for i in range(coset, len(inputtext), l):
                alphabet[inputtext[i]] += 1
                total += 1
            signature = [0] * 26
            i = 0
            for val in sorted(alphabet.values()):
                signature[i] = val / total
                i += 1
            upperarea, lowerarea = 0, 0
            for i in range(0, 12):
                lowerarea += signature[i] + ((signature[i + 1] - signature[i]) / 2)
                upperarea += signature[i + 13] + ((signature[i + 14] - signature[i + 13]) / 2)
            avgcosetdiff += upperarea - lowerarea
        avgcosetdiff /= l
        Avals[l - 1] = avgcosetdiff
        print("Size", l, ": A =", avgcosetdiff)

        if avgcosetdiff >= maxdiff:
            maxdiff = avgcosetdiff
            probkey = l

    print("Local Max =", probkey)
    Avals[probkey - 1] = 0
    for i in range(1, probkey):
        if (probkey % i == 0) and (Avals[i - 1] > Avals[i - 2]) and (Avals[i - 1] > Avals[i]):
            probkey = i
            break
print("Probable key length:", probkey)
print()

# begin analyzing for keyword
print("Analyzing for keyword:")
englishfreq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
               0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929,
               0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
               0.01974, 0.00074] # set of frequencies for the english language, in alphabetical order
for coset in range(0, probkey):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetcount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                     'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                     'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                     'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    total = 0
    for i in range(coset, len(inputtext), probkey):
        alphabetcount[inputtext[i]] += 1
        total += 1
    cosetvector = [0] * 26
    for item in alphabetcount.items():
        cosetvector[alphabet.find(item[0])] = item[1] / total
    scrawl = [0] * 26
    for i in range(len(cosetvector)):
        scrawl[i] = 0
        for j in range(len(cosetvector)):
            scrawl[i] += cosetvector[(i + j) % 26] * englishfreq[j]
    keyvals = [0] * 4
    for i in range(len(keyvals)):
        j = scrawl.index(max(scrawl))
        keyvals[i] = alphabet[j]
        scrawl[j] = 0
    print("Key letter:", keyvals[0], "  Alt. letters:", keyvals[1], keyvals[2], keyvals[3])
