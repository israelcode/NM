#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import numpy as np
import matplotlib.pyplot as plot
import math


# метод Ньютона
def Newton(x_first, epsilon):
    x_curr = x_first
    x_next = []
    i = 0

    while True:
        # объявляем функцию
        x1, x2 = x_curr
        f_x = np.array([x1 - math.cos(x2) - 2, x2 - math.sin(x1) - 2])
        # матрица Якоби
        J_x = np.array([[1, math.sin(x2)], [-math.cos(x1), 1]])
        x_next = x_curr + np.linalg.solve(J_x, -1 * f_x)
        # завершение
        if np.linalg.norm(x_next - x_curr) <= epsilon:
            break
        x_curr = x_next
        i += 1

    return x_next, i-1



def SimpleIterations(Phi, epsilon):
    x_range = [(2.7, 2.9), (0.9, 1.1)]
    x_curr = np.array([[np.mean(x)] for x in x_range])
    x_next = []
    i = 0
    u = [np.linspace(x[0], x[1]) for x in x_range]
    
    # максимум из матрицы Фи

    q = max(map(lambda x: np.linalg.norm(Phi(x), ord=np.inf), zip(*u)))

    if q >= 1:
        print('!!!!')
        exit()

    # коэфф
    c = q / (1 - q)
    while True:
        # объявляем функцию
        x1, x2 = x_curr
        x_next = np.array([[2 + math.cos(x2)], [2 + math.sin(x1)]])

        # завершение
        if np.linalg.norm(x_next - x_curr, ord=np.inf) * c <= epsilon:
            break

        x_curr = x_next
        i += 1

    return x_next, i

def Phi_matrix(x):
    x1, x2 = x

    return np.array([[0, -math.sin(x2)], [math.cos(x1), 0]])


def main():
    u = np.arange(-2.0, 4.0, 0.1)
    u1 = [(lambda x2: math.cos(x2) + 2)(x) for x in u]
    u2 = [(lambda x1: math.sin(x1) + 2)(x) for x in u]


    plot.figure()
    plot.xlabel('x1')
    plot.ylabel('x2')
    plot.plot(u, u1, 'r')
    plot.plot(u2, u,'g')
    plot.axis('equal')
    plot.grid(True)
    plot.show()

    epsilon = 0.01
    x_first = np.array([[2.8], [1.0]])
    solve1, i1 = Newton(x_first, epsilon)
    solve2, i2 = SimpleIterations(Phi_matrix, epsilon)

    print('Newton: ',solve1,', i: ',i1)
    print('SimpleIterations: ',solve2,', i: ',i2)

main()
