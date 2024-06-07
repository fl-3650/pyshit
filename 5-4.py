def f(y, x):
    n = len(x)
    result = 0
    y.insert(0, 0)
    x.insert(0, 0)

    for i in range(1, n + 1):
        abs_sum = abs(24 * y[i] ** 2 + x[n + 1 - i] / 53)
        result += 24 * abs_sum ** 2

    return 78 * result


print(f([0.97, 0.59, 0.27, 0.42, -0.01, -0.1, -0.3],
        [0.33, -0.8, 0.31, -0.57, 0.57, -0.41, 0.71]))
