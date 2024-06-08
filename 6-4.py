def main(delta):
    K = {d - d % 2 for d in delta if 39 <= d <= 61}
    N = {abs(k) + 7 * k for k in K if k > -27 or k <= 41}
    X = {d % 2 - abs(d) for d in delta if -81 <= d <= 18}
    O = {abs(x) + x ** 2 for x in X if -90 <= x < 54}

    b = len({(a, b) for a in N for b in O}) + sum(9 * o for o in O)

    return b


print(main({-64, -62, 67, 9, 73, 44, 46, 80, 16, -98}))
print(main({-92, 6, -56, 76, 92, -3, -10, -38, -4, 61}))
