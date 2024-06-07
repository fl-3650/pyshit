import math as mt


def f(x, z, y):
    total = 0
    n = len(x)
    x.insert(0, 0)
    z.insert(0, 0)
    y.insert(0, 0)

    for i in range(1, n + 1):
        first = y[mt.ceil(i / 2)] ** 3
        second = -30 * x[n + 1 - mt.ceil(i / 3)] ** 2
        third = -z[mt.ceil(i / 3)]

        total += (first + second + third) ** 5

    return 42 * total


print(f([-0.15, -0.12, 0.21, -0.79],
        [-0.6, 0.91, -0.25, 0.09],
        [-0.6, -0.99, 0.87, -0.31]))
