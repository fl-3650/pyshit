def main(K):
    psi = {abs(k) + abs(k) for k in K if (k >= -16 or k <= 85)}
    E = {k * w for k in K for w in psi if k <= w}
    M = {abs(w) for w in psi if -50 <= w <= 85}

    d = len(E.union(M)) + sum(mu for mu in M)

    return d


print(main({37, -90, 6, 10, 15, 16, -78, -13, 51, -98}))
print(main({37, 72, 82, -77, -14, 22, -73, 24, 26, 60}))
