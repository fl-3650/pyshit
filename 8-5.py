def main(t: tuple):
    x = [i for i in t]

    g1 = 0b1111111 & x[0]
    g2 = 0b11111111 & x[1]
    g3 = 0b111111111 & x[2]
    g4 = 0b0000000000

    res = g1 | (g2 << 7) | (g3 << 15) | (g4 << 24)

    return hex(res)


print(main((110, 253, 420)))