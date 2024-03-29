import numpy as np
import math

def lagr(f, x_vec, x):
    return np.sum(
        [f[i] * np.prod([(x - x_vec[i]) / (x_vec[i] - x_vec[j]) if j != i else 1. for j in range(len(x_vec))])\
                      for i in range(len(x_vec))])


def newt(f, x_vec, x):
    n = len(x_vec)
    coeff = [np.sum([f[k] / np.prod([(x_vec[k] - x_vec[j]) if j != k else 1. for j in range(i + 1)]) for k in range(i + 1)]) for i in range(n)]
    return np.sum(\
                     [coeff[i] * np.prod([x - x_vec[j] for j in range(i)])\
               for i in range(n)])


#производня 4 порядка для поиска M_{n+1} = max |f^{n+1}(x)|
def helpM(x):
    return -(24 * x * (-1 + x ** 2))/(1 + x ** 2) ** 4



x_1 = [-3, -1, 1, 3]
x_2 = [-3, 0, 1, 3]

M = 4.66
pn = [lagr, newt]
n = ["lagrange", "newton"]
x_val = -0.5





for test in zip([x_1, x_2], pn, n):
    x_vec = test[0]
    f = [np.arctan(x) for x in x_vec]
    poly = test[1]
    name = test[-1]

    print('Method :', name)
    eps = np.abs(np.arctan(x_val) - poly(f, x_vec, x_val))
    print('arctg(x*) = ',np.arctan(x_val))
    print('P(x)',poly(f, x_vec, x_val))
    print('|arctg(x*) - P(x)| = ', eps)
    upper_bound = np.abs((x_val - x_vec[0])*(x_val - x_vec[1])*(x_val - x_vec[2])*(x_val - x_vec[3])) * M / math.factorial(len(x_vec) + 1)
    #print('M / (n + 1)!|w(x)| = ', upper_bound) # погрешность
    #print(eps <= upper_bound)    


