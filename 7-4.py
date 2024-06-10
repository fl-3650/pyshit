s = (
    {1982, "MUPAD", 1972},
    {1982, "MUPAD", 2015},
    {1982, "IDRIS", "SQLPL"},
    {1982, "IDRIS", "SMT"},
    {1982, "IDRIS", "SMALI"},
    {1995, "SQLPL", "MUPAD"},
    {1995, "SQLPL", "IDRIS"},
    {1995, "SMT"},
    {1995, "SMALI", "MUPAD"},
    {1995, "SMALI", "IDRIS"},
)


def main(r):
    s1 = set(r)
    return max([i for i in range(len(s)) if not (len(s[i] - s1))])


print(main(['SQLPL', 1982, 2015, 'IDRIS']))
print(main(['SMALI', 1982, 2015, 'IDRIS']))
print(main(['SMT', 1995, 2015, 'IDRIS']))
print(main(['SQLPL', 1995, 2015, 'IDRIS']))
print(main(['SMT', 1982, 1972, 'MUPAD']))
