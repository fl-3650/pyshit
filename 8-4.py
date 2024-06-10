def main(n: int):
    h1 = 0b1 & n
    h2 = 0b11 & (n >> 1)
    h3 = 0b1111111 & (n >> 3)
    h4 = 0b1 & (n >> 10)
    h5 = 0b1111111111 & (n >> 11)

    return [('H1', h1), ('H2', h2), ('H3', h3), ('H4', h4), ('H5', h5)]


print(main(560441))
print(main(1704804))
print(main(370))
print(main(1977475))
