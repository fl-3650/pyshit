s = ({"QML", 1970, 1972},
     {"QML", 1970, 2011},
     {"QML", 1968, "STON"},
     {"QML", 1968, "OOC"},
     {"QML", 1968, "FLUX"},
     {"CLIPS"},
     {"SAGE", 1970, 1972},
     {"SAGE", 1970, 2011},
     {"SAGE", 1968, 1972},
     {"SAGE", 1968, 2011})


def main(r):
    s1 = set(r)
    return [i for i in range(len(s)) if not len(s[i] - s1)][0]


print(main(['SAGE', 1968, 'STON', 1972]))
