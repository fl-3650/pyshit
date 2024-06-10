s = (
    {2003, 1997, 'NU', 2004},
    {2003, 1997, 'NU', 1975},
    {2003, 1997, 'NU', 1968},
    {2003, 1997, 'DM'},
    {2003, 1997, 'CHUCK'},
    {2003, 1981},
    {1997},
    {1990, 'TEA'},
    {1990, 'ANTLR'},
    {1990, 'ANTLR', 'NU', 1997},
    {1990, 'ANTLR', 'NU', 1981},
    {1990, 'ANTLR', 'DM'},
    {1990, 'ANTLR', 'CHUCK'}
)


def main(r):
    s1 = set(r)
    return max([i for i in range(len(s)) if not (len(s[i] - s1))])


print(main(['ANTLR', 1981, 1990, 'CHUCK', 2004]))
print(main(['ANTLR', 1997, 2003, 'NU', 1968]))
print(main(['TEA', 1997, 2003, 'CHUCK', 2004]))
print(main(['TEA', 1981, 1997, 'CHUCK', 2004]))
print(main(['TEA', 1981, 1990, 'NU', 2004]))
