import matplotlib.pyplot as plt
import numpy as np
import math as m
from math import e

я

def function(x):
    return e**x-x**3+3*x**2-2*x-3 #  Функция


def first_derivative(x):
    return -3*x**2+6*x+e**x-2 # Первая производная


def second_derivative(x):
    return -6*x+e**x+6 # Вторая производная


def function2(x):
    return m.log(x**3.0-3.0*x**2.0+2.0*x+3.0) # Функция, но в виде, где Х влевой части, а все остальное в правой


def function2_derivative(x):
    return (3*x**2-6*x+2)/(x**3+2*x+3) # Ее производная



def newton(function, start_x, first_derivative, second_derivative, eps):
    #счетчик итераций
    iters = 0    
    x_prev = start_x
    x_cur = x_prev - function(x_prev) / first_derivative(x_prev)
    print("i\t start_x\t function(start_x)")
    print("x%d\t%e\t%e"%(iters,x_prev,function(x_prev)))
    iters = 1

    while abs(x_cur - x_prev) >= eps:
        x_prev = x_cur
        x_cur = x_prev - function(x_prev) / first_derivative(x_prev)
        
        print("x%d\t%e\t%e"%(iters,x_cur,function(x_cur)))
        if abs(x_prev - x_cur)<= eps:
            plt.plot(x_prev, function(x_prev), 'or')
            return x_cur

        iters += 1
      
    return x_cur, iters

def simple_iter(eps):
    begin = 0.9
    end = 1.1

    q = max([abs(function2_derivative(x)) for x in np.arange(begin, end, eps)])
    coeff = q / (1 - q)
    iters = 0
    x_prev = (begin + end) / 2.0
    x_cur = function2(x_prev)
    print("x%d\t%e\t%e"%(iters,x_prev,function(x_prev)))


    while abs(x_cur - x_prev) * coeff >= eps:
        x_prev = x_cur
        x_cur = function2(x_prev)
        iters += 1
        print("x%d\t%e\t%e"%(iters,x_cur,function2(x_cur)))

    return x_cur, iters






solve  = newton(function, 1.0, first_derivative, second_derivative, 0.001)
print('Методом Ньютона, ответ: '+str(solve))

result, iter_count = simple_iter(0.001)
print('Метод итераций, ответ: '+ str(result))


# График
u = np.arange(0, 2, 0.001) # значения Х
f = e**u-u**3+3*u**2-2*u-3

#plt.plot(u, w)
plt.plot(u,f)

plt.title('Graphic')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(['Solve'], loc='upper left')
plt.show()
