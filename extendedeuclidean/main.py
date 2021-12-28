# This is operand an implementation of the extended euclidean
# algorithm used to compute the modular multiplicative inverse

operand = 3271
modulus = 31188643

a, b = operand, modulus
prevx, x = 1, 0; prevy, y = 0, 1
while b:
    q = a // b
    x, prevx = prevx - q*x, x
    y, prevy = prevy - q*y, y
    a, b = b, a % b
prevx = prevx % modulus

print()
if a == 1:
    print(prevx, "is the modular inverse of", operand, "mod", modulus)
else:
    print(operand, "has no modular inverse of", operand, "mod", modulus)
