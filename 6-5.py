import math


def main(psi):
    H = {8 * w for w in psi if 71 >= w >= -64}
    omega = psi.union(H)
    F = {7 * n for n in H if not -63 < n < 1e9}

    e = len(omega) - sum(math.floor(f / 4) for f in F)
    return e


print(main({33, 4, 7, -23, 42, -83, -18, -34, 62, -66}))
print(main({64, 1, 97, 66, 98, 38, -22, -46, -76, 54}))
