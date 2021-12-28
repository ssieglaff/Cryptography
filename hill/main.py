# This code implements the Hill matrix cipher.

def xgcd(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = a//b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx


def printmatrix(x):
    print("[ %-2d %-2d ]\n[ %-2d %-2d ]" % (x[0][0], x[0][1], x[1][0], x[1][1]))


def cipher(key, a, b):
    x, y = ((key[0][0] * a) + (key[0][1] * b)) % 26, ((key[1][0] * a) + (key[1][1] * b)) % 26
    return x, y


inputtext = "FHHJJFSIVQQMKMBCBZXCQMKMXU"
keymatrix = [[3, 12],
             [5, 11]] # only use 2x2 matrices
encrypt = -1 # 1 to encrypt, -1 to decrypt

outputtext = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
inputtext = inputtext.lower()
if len(inputtext) % 2 == 1:
    inputtext += 'X'
print(inputtext)
detkey = ((keymatrix[0][0] * keymatrix[1][1]) - (keymatrix[0][1] * keymatrix[1][0])) % len(alphabet)
gcd, invdet = xgcd(detkey, len(alphabet))
invdet = invdet % len(alphabet)
if gcd == 1:
    print("Mod. Determinant = ", detkey, "; Inv. Determinant = ", invdet)
    if encrypt == -1:
        a, b, c, d = keymatrix[0][0], keymatrix[0][1], keymatrix[1][0], keymatrix[1][1]
        keymatrix[0][0], keymatrix[0][1], keymatrix[1][0], keymatrix[1][1] = \
            (d * invdet) % len(alphabet), (-b * invdet) % len(alphabet), \
            (-c * invdet) % len(alphabet), (a * invdet) % len(alphabet)
else:
    print("Message undecryptable. Key matrix uninvertable.")
    print("Determinant = ", detkey)
    if encrypt == -1:
        quit()
print("Matrix used:")
printmatrix(keymatrix)

for i in range(0, len(inputtext), 2):
    a, b = alphabet.find(inputtext[i]), alphabet.find(inputtext[i+1])
    x, y = cipher(keymatrix, a, b)
    outputtext += alphabet[x]
    outputtext += alphabet[y]

print("\nOutput:")
print(outputtext)
