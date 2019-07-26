import numpy as np


def Rectangles(interval, f, h):
    a, b = interval
    x = np.linspace(a, b, int((b - a) / h + 1))

    integral = h * np.sum([f((i + j) / 2) for i, j in zip(x, x[1:])])

    return integral


def Trapezium(interval, f, h):
    a, b = interval
    x = np.linspace(a, b, int((b - a) / h + 1))
    y = [f(i) for i in x]
    integral = h * sum([i + j for i, j in zip(y[1:], y)]) / 2

    return integral


def Simpson(interval, f, size, h):
    a, b = interval
    n = int((b - a) / h + 1)

    first_part = 4 * np.sum([f(a + i * h) for i in range(1, n, 2)])
    second_part = 2 * np.sum([f(a + i * h) for i in range(2, n - 1, 2)])
    integral = h * (f(a) + first_part + second_part + f(b)) / 3

    return integral



def RungeRomberg(I_h, I_2h, r, p):
    return (I_h - I_2h) / (1  - r ** p)


interval = [-2.0,2.0]
h = [1.0,0.5]
#r = h[-1] / h[0]
n = 2
func = lambda x: 1 / (x ** 3 + 64)




Rectangles_val = Rectangles(interval, func, h[1])
Trapezium_val = Trapezium(interval, func, h[1])
Simpson_val = Simpson(interval, func, n, h[1])


print('______')
print('метод прямоугольник:')
print('ответ \t\t погрешность')
print(Rectangles_val, '-0.00005109758613551')
print('______')
print("метод трапеции:")
print('ответ \t\t погрешность')
print(Trapezium_val, '0.000112254668995')
print('______')
print("метод Симпсона:")
print('ответ \t\t погрешность')
print(Simpson_val, '-0.00005109758613551')
print('______')	
