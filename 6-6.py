def main(B):
    K = {b % 3 + 9 * b for b in B if (b >= 1 or b < 78)}
    N = {b for b in B if (b <= 97 or b > -21)}
    I = {v * k for v in N for k in K if v > k}

    KxI = {(a, b) for a in K for b in I}

    d = sum(k % 3 for k in K) - sum(abs(k) + 8 * i for (k, i) in KxI)

    return d


print(main({-64, -29, -25, -89, 45, -67, -11, -4, 61, 95}))
print(main({-62, -28, -25, 43, -51, -44, 21, 22, -12, -97}))
