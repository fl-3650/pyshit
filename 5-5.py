import math


def f(y, x, z):
    n = len(y)
    total = 0
    y.insert(0, 0)
    x.insert(0, 0)
    z.insert(0, 0)

    for i in range(1, n + 1):
        first = 94 * y[n + 1 - i]
        second = z[math.ceil(i / 4) ** 3] ** 3
        third = 4 * x[math.ceil(i / 4)] ** 2
        total += ((first + second + third) ** 6) / 52

    return 60 * total


print(f([0.67, 0.83],
        [0.16, 0.86],
        [-0.47, -0.57]))
