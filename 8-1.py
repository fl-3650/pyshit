def main(s: str):
    i = int(s)
    j1 = 0b1 & (i >> 0)
    j2 = 0b111 & (i >> 1)
    j3 = 0b1111 & (i >> 4)
    j4 = 0b11111 & (i >> 8)

    res = (j3 << 9) | (j1 << 8) | (j4 << 3) | j2

    return hex(res)


print(main('2141'))
print(main('692'))
print(main('5917'))
print(main('4469'))
