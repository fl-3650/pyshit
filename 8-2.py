def main(s):
    i = int(s, 16)
    i1 = 0b11111111 & (i >> 0)
    i2 = 0b11111111 & (i >> 8)
    i3 = 0b111 & (i >> 16)
    i4 = 0b11111 & (i >> 19)
    i5 = 0b1111 & (i >> 24)

    res = [
        ("I1", i1),
        ("I2", i2),
        ("I3", i3),
        ("I4", i4),
        ("I5", i5)
    ]

    return res


print(main('0x7dcf46'))