def main(n: int):
    b1 = 0b111 & n
    b2 = 0b11111 & (n >> 3)
    b3 = 0b11111 & (n >> 8)
    b4 = 0b1 & (n >> 13)
    b5 = 0b1111 & (n >> 14)
    b6 = 0b11111 & (n >> 18)

    return str(b1), str(b2), str(b3), str(b4), str(b5), str(b6)


print(main(3221498))
print(main(7221320))
print(main(6338784))
print(main(6960588))
