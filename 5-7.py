import math


def f(x, z):
    total = 0
    n = len(x)
    x.insert(0, 0)
    z.insert(0, 0)

    for i in range(1, n + 1):
        total += 75 * (z[n + 1 - i] ** 2 - x[math.ceil(i / 2)] - 91 * z[n + 1 - i] ** 3) ** 3

    return 97 * total


print(f([0.29, 0.75, -0.07, -0.73],
        [0.5, 0.56, 0.43, -0.05]))
print(f([-0.98, -0.6, 0.16, 0.05],
        [-0.2, -0.18, 0.27, -0.44]))
