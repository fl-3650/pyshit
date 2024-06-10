def main(dct: dict):
    q2 = int(dct.get('Q2')) & 0b1111111111
    q3 = int(dct.get('Q3')) & 0b111111
    q4 = int(dct.get('Q4')) & 0b111111

    return hex(q2 << 4 | q3 << 14 | q4 << 20)


print(main({'Q2': '785', 'Q3': '52', 'Q4': '63'}))