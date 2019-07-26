import numpy as np
import matplotlib.pyplot as plot


def TDMA(matrix, d, shape):
    a, b, c = zip(*matrix)
    p = [-c[0] / b[0]]
    q = [d[0] / b[0]]
    x = [0] * (shape + 1)
    for i in range(1, shape):
        p.append(-c[i] / (b[i] + a[i] * p[i - 1]))
        q.append((d[i] - a[i] * q[i - 1]) / (b[i] + a[i] * p[i - 1]))
    for i in reversed(range(shape)):
        x[i] = p[i] * x[i + 1] + q[i]
    return x[:-1]


def SPLINE(x, f):
    n = len(x)
    h = [x[i] - x[i - 1] for i in range(1, n)]
    tridiag_matrix = [[0, 2 * (h[0] + h[1]), h[1]]]
    b = [3 * ((f[2] - f[1]) / h[1] - (f[1] - f[0]) / h[0])]
    for i in range(1, n - 3):
        tridiag_row = [h[i], 2 * (h[i] + h[i + 1]), h[i + 1]]
        tridiag_matrix.append(tridiag_row)
        b.append(3 * ((f[i + 2] - f[i + 1]) / h[i + 1] - (f[i + 1] - f[i]) / h[i]))
    tridiag_matrix.append([h[-2], 2 * (h[-2] + h[-1]), 0])
    b.append(3 * ((f[-1] - f[-2]) / h[-1] - (f[-2] - f[-3]) / h[-2]))
    c = TDMA(tridiag_matrix, b, n - 2)
    a = []
    b = []
    d = []
    c.insert(0, 0)
    for i in range(1, n):
        a.append(f[i - 1])
        if i < n - 1:
            d.append((c[i] - c[i - 1]) / (3 * h[i - 1]))
            b.append((f[i] - f[i - 1]) / h[i - 1] -
                     h[i - 1] * (c[i] + 2 * c[i - 1]) / 3)
    b.append((f[-1] - f[-2]) / h[-1] - 2 * h[-1] * c[-1] / 3)
    d.append(-c[-1] / (3 * h[-1]))
    return a, b, c, d





def polyval(x0, x, k, coef):
    a, b, c, d = coef
    diff = x0 - x[k]

    return a[k] + b[k] * diff + c[k] * diff ** 2 + d[k] * diff ** 3


def poly(x, x_test, coef):
    k = 0
    for i, j in zip(x, x[1:]):
        if i <= x_test <= j:
            break
        k += 1

    return polyval(x_test, x, k, coef)



x = [-3, -1, 1, 3, 5]
f = [2.8198, 2.3562, 0.78540, 0.32175, 0.19740]
x_test = -0.5    

coef = SPLINE(x, f)

res = poly(x, x_test, coef)
print(f'a = {coef[0]}\nb = {coef[1]}\nc = {coef[2]}\nd = {coef[3]}\n')
print('x* = ', x_test)
print('f(x*) = ', res)

x_vals = np.linspace(x[0], x[-1])
y = [poly(x, val, coef) for val in x_vals]

plot.figure()
plot.xlabel('x')
plot.ylabel('y')
plot.plot(x_vals, y, 'g')
plot.grid(True)
plot.show()
