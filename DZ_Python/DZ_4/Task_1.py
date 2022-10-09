# Задача № 1. Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math


def f(n):
    p = 0
    for i in range(1, n, 4):
        p = p + 4/i - 4/(i+2)
    return p


def pi_step_by_step():
    x = 0.1
    for i in range(1, 11):
        print(f"d = {'%.10f' % x}, Пи = {round(math.pi,i)}")
        x = x / 10


if __name__ == '__main__':
    n = 1000000
    print("Вычисление методом Лейбница ", n, " итераций ", f(n))
    pi_step_by_step()
