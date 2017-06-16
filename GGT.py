# 16.06.2017
# Calculate the biggest common divisor


def GGT(x, y):
    while y != 0:
        remainder = x % y
        x = y
        y = remainder
    return x


print(GGT(125, 50))
