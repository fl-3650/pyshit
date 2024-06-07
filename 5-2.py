import math as mt


def f(x):

    n = len(x)
    x.insert(0, 0)
    result = 0
    for i in range(1, n + 1):
        result += 5 * (92 + x[mt.ceil(i / 3)] ** 2 + 76 * x[mt.ceil(i / 3)]**3) ** 6

    return 84 * result


print(f([-0.47, -0.6, 0.08, 0.07]))
