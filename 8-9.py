def main(lst: list[tuple]):
    i1 = int(lst[0][1], 16) & 0b11111111
    i2 = int(lst[1][1], 16) & 0b1111111
    i3 = int(lst[2][1], 16) & 0b1111111111
    i4 = int(lst[3][1], 16) & 0b11

    return str(i1 | (i2 << 8) | (i3 << 15) | (i4 << 25))


print(main([('I1', '0x74'), ('I2', '0x75'), ('I3', '0x248'), ('I4', '0x1')]))