import math as mt


def main(M):
    A = {abs(mu) for mu in M if not (-33 <= mu < 1e9)}
    O = {mu ** 3 - mu ** 2 for mu in M if -1e9 < mu < 89}
    N = {abs(theta) + abs(theta) for theta in O if not (-82 <= theta < 1e9)}

    p = len(A.union(N)) + sum(mt.ceil(v / 2) for v in N)

    return p


print(main({-59, 7, 77, 79, -46, -75, -74, -34, 95, -33}))
print(main({36, 40, 73, -87, 72, -20, 16, -14, 24, -33}))
