def main(st):
    lst = [int(i) for i in st]

    q1 = 0b111 & lst[0]
    q2 = 0b1 & lst[1]
    q3 = 0b111111111 & lst[2]
    q4 = 0b11111 & lst[3]
    q5 = 0b111111111 & lst[4]
    q6 = 0b111111111 & lst[5]

    return q1 | q2 << 3 | q3 << 4 | q4 << 13 | q5 << 18 | q6 << 27


print(main(('0', '0', '16', '23', '121', '358')))


