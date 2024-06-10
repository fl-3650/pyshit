def main(s):
    x = int(s)
    g1 = 0b11111 & x
    g3 = 0b11 & (x >> 9)
    g4 = 0b1111111111 & (x >> 11)
    g5 = 0b1111111111 & (x >> 21)
    g6 = 0b11111 & (x >> 31)

    return {
        'G1': g1,
        'G3': g3,
        'G4': g4,
        'G5': g5,
        'G6': g6
    }


print(main('51315795914'))