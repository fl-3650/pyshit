s = (
    {2003, 2020, "STON"},
    {2003, 2020, "HAML"},
    {2003, 1999, "HAXE"},
    {2003, 1999, "FORTH"},
    {2003, 1999, "FANCY"},
    {2003, 1983},
    {2017},
    {1975, "HAXE", 2020},
    {1975, "HAXE", 1999},
    {1975, "HAXE", 1983},
    {1975, "FORTH"},
    {1975, "FANCY"}
)


def main(r):
    s1 = set(r)
    return max([i for i in range(len(s)) if not (len(s[i] - s1))])


print(main([2003, 2020, 'HAML', 'HAXE']))
print(main([1975, 1999, 'HAML', 'FORTH']))
print(main([2017, 2020, 'STON', 'FORTH']))
print(main([1975, 2020, 'HAML', 'HAXE']))
print(main([1975, 1999, 'STON', 'FANCY']))
