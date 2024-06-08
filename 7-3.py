s = (
    {"MESON", 2013, "COQ"},
    {"MESON", 2013, "OCAML"},
    {"MESON", 2013, "GO"},
    {"MESON", 2012},
    {"MESON", 1981, "COQ"},
    {"MESON", 1981, "OCAML"},
    {"MESON", 1981, "GO"},
    {"EJS", 2013, 1958},
    {"EJS", 2013, 2013},
    {"EJS", 2012},
    {"EJS", 1981},
    {"EAGLE"}
)


def main(r):
    s1 = set(r)
    return [i for i in range(len(s)) if not len(s[i] - s1)][0]


print(main([2012, 'OCAML', 'MESON', 2013]))
print(main([2013, 'GO', 'MESON', 1958]))
print(main([2012, 'OCAML', 'EJS', 1958]))
print(main([1981, 'GO', 'EAGLE', 2013]))
print(main([1981, 'COQ', 'EJS', 1958]))
