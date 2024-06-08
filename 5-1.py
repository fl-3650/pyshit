import math


def f(x):
    total = 0
    n = len(x)
    x.insert(0, 0)

    for i in range(1, n + 1):
        total += math.floor(x[i] ** 3 + 32 + 74 * x[i] ** 2) ** 6

    return total


print(f([-0.5, 0.36, 0.22, -0.83]))
