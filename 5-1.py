import math


def main(y):
    total = 0
    n = len(y)
    for i in range(1, n + 1):
        total += (1 - y[n - i] ** 3 - 16 * y[n - i]**2)

    return total


print(main([0.74, -0.93, -0.25, -0.37, 0.64, 0.01]))
print(main([0.93, 0.26, 0.71, -0.7, -0.29, -0.25]))
print(main([0.82, -0.86, -0.27, -1.0, -0.26, -0.53]))
print(main([-0.89, -0.02, -0.74, 0.88, 0.8, 0.74]))
