# This code tests possible solutions to an affine ciphertext

inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
commonletters = "etai" #set of most common letters in english, add more in order of likeliness to test more options

def modinv(a, mod):
    prevx, x = 1, 0; prevy, y = 0, 1
    while mod:
        q = a // mod
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, mod = mod, a % mod
    return a, prevx

inputtext = inputtext.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for char in inputtext.lower():
    counts[char] += 1
yvals = [0] * len(commonletters)
xvals = [0] * len(commonletters)
items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for i in range(len(commonletters)):
    xvals[i] = alphabet.find(commonletters[i])
    yvals[i] = alphabet.find(items[i][0])

for i in range(len(xvals) - 1):
    for j in range(i + 1, len(xvals)):
        # print(i, j)
        for k in range(len(yvals) - 1):
            for l in range(k + 1, len(yvals)):
                #print(i, j, " => ", k, l)
                b = 0
                unique, inv = modinv((xvals[i] - xvals[j]) % len(alphabet), len(alphabet))
                a = (inv * (yvals[k] - yvals[l])) % len(alphabet)
                if unique == 1 and a % 2 != 0 and a != 13:
                    b = (yvals[k] - a * xvals[i]) % len(alphabet)
                    unique, inv = modinv(a, len(alphabet))
                    outputtext = ""
                    for char in inputtext:
                        outputtext += alphabet[((alphabet.find(char) - b) * inv) % len(alphabet)]
                    print("a =", a, "b =", b, "text:", outputtext)

                unique, inv = modinv((xvals[j] - xvals[i]) % len(alphabet), len(alphabet))
                a = (inv * (yvals[k] - yvals[l])) % len(alphabet)
                if unique == 1 and a % 2 != 0 and a != 13:
                    b = (yvals[0] - a * xvals[0]) % len(alphabet)
                    unique, inv = modinv(a, len(alphabet))
                    outputtext = ""
                    for char in inputtext:
                        outputtext += alphabet[((alphabet.find(char) - b) * inv) % len(alphabet)]
                    print("a =", a, "b =", b, "text:", outputtext)
        #for a in range(len(alphabet)):
        #    for b in range(len(alphabet)):
        #        if ((a * xvals[i] + b) % len(alphabet) == yvals[i]
        # print(j, i)
