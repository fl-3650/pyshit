def main(A_strange):
    H = {lmbd for lmbd in A_strange if -69 < lmbd <= 79}
    delta = {lmbd * n for lmbd in A_strange for n in H if lmbd < n}

    A = H.union(delta)

    v = len(delta) - sum(d * a for d in delta for a in A)
    return v


print(main({36, 40, -23, 14, -79, -11, 25, -99, -34}))
