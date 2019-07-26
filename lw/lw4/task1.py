from math import exp

import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable



def function (x, y, y1):
    return y*np.power(np.cos(x),2) - y1*np.tan(x)

def real_function(x):
    return np.exp(np.sin(x))+ np.exp(-np.sin(x))


def analytical_solution(f, a, b, h):
    x = [i for i in np.arange(a, b + h, h)]
    y = [f(i) for i in x]
    return x, y


def euler(f, a, b, h, y0, y1):
    n = int((b - a) / h)
    x = [i for i in np.arange(a, b + h, h)]
    y = [y0]
    z = y1
    for i in range(n):
        z += h * f(x[i], y[i], z)
        y_i = y[i] + h * g(x[i], y[i], z)
        y.append(y_i)
    return x, y


def g(x, y, z):
    return z



def reunge_kutta(f, g, a, b, h, y0, y1):
    n = int((b - a) / h)
    x = [i for i in np.arange(a, b + h, h)]
    y = [y0]
    z = [y1]
    for i in range(n):
        K1 = h * g(x[i], y[i], z[i])
        L1 = h * f(x[i], y[i], z[i])
        K2 = h * g(x[i] + 0.5 * h, y[i] + 0.5 * K1, z[i] + 0.5 * L1)
        L2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * K1, z[i] + 0.5 * L1)
        K3 = h * g(x[i] + 0.5 * h, y[i] + 0.5 * K2, z[i] + 0.5 * L2)
        L3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * K2, z[i] + 0.5 * L2)
        K4 = h * g(x[i] + h, y[i] + K3, z[i] + L3)
        L4 = h * f(x[i] + h, y[i] + K3, z[i] + L3)
        delta_y = (K1 + 2 * K2 + 2 * K3 + K4) / 6
        delta_z = (L1 + 2 * L2 + 2 * L3 + L4) / 6
        y.append(y[i] + delta_y)
        z.append(z[i] + delta_z)
    return x, y, z


def adams(f, g, x, y, z, h):
    n = len(x)+1
    x = x[:4]
    y = y[:4]
    z = z[:4]
    for i in range(3, n - 1):
        z_i = z[i] + h * (55 * f(x[i], y[i], z[i]) -
                          59 * f(x[i - 1], y[i - 1], z[i - 1]) +
                          37 * f(x[i - 2], y[i - 2], z[i - 2]) -
                           9 * f(x[i - 3], y[i - 3], z[i - 3])) /24
        z.append(z_i)
        y_i = y[i] + h * (55 * g(x[i], y[i], z[i]) -
                          59 * g(x[i - 1], y[i - 1], z[i - 1]) +
                          37 * g(x[i - 2], y[i - 2], z[i - 2]) -
                           9 * g(x[i - 3], y[i - 3], z[i - 3])) / 24
        y.append(y_i)
        x.append(x[i] + h)
    return x, y


def runge_romberg(res):
    k = res[0]['h'] / res[1]['h']
    err_euler = []
    for i in range(len(res[0]['Euler']['y'])):
        err_euler.append(abs(res[0]['Euler']['y'][i] - res[1]['Euler']['y'][i]) / (k ** 1 - 1))

    err_runge = []
    for i in range(len(res[0]['Runge']['y'])):
        err_runge.append(abs(res[0]['Runge']['y'][i] - res[1]['Runge']['y'][i]) / (k ** 4 - 1))

    err_adams = []
    for i in range(len(res[0]['Adams']['y'])):
        err_adams.append(abs(res[0]['Adams']['y'][i] - res[1]['Adams']['y'][i]) / (k ** 4 - 1))

    return {'Euler': err_euler, 'Runge': err_runge, 'Adams': err_adams}



save_res = []
a=0
b=1
st = 0.05
y0 =2
y1=0
steps = [st, st / 2]
f = open('out.txt', 'w')

for h in steps:
        euler_x, euler_y = euler(function , a, b, h, y0, y1)
      

        
        runge_x, runge_y, runge_z = reunge_kutta(function , g, a, b, h, y0, y1)
     

        
        adams_x, adams_y = adams(function , g, runge_x, runge_y, runge_z, h)
       
        anal_x, anal_y = analytical_solution(real_function, a, b, h)
     
        save_res.append({
                        "h": h,
                        "Euler": {'x': euler_x, 'y': euler_y},
                        "Runge": {'x': runge_x, 'y': runge_y},
                        "Adams": {'x': adams_x, 'y': adams_y},
                         })
errors = runge_romberg(save_res)

print(errors)


