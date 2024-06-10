def main(s):
    n = int(s)
    f2 = 0b111 & (n >> 8)
    f3 = 0b11111111 & (n >> 11)
    f4 = 0b111 & (n >> 19)

    return f2 | f3 << 11 | f4 << 19


print(main('711533'))