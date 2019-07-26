import numpy as np
import math



def Monte_carlo_method(intervals, f, experiments_amount): 
    size = len(intervals)
    left, right = zip(*intervals)
    vol=[]
    for element in intervals:
        vol.append(element[1]-element[0])
    #print('vol',vol)
    volume=vol[0]
    #print(volume)
    #print(vol)
    for s in vol[1:]:
        #print(s)
        volume=volume*s   

    integral = volume * np.sum([f(np.random.uniform(left, right, size)) for _ in range(experiments_amount)]) / experiments_amount

    return integral




def Quadrature_method(interval, f, h):
    #Метод парабол
    a, b = interval
    n = int((b - a) / h + 1)
    integral = h * (f(a) + 4 * np.sum([f(a + i * h) for i in range(1, n, 2)])+ 2 * np.sum([f(a + i * h) for i in range(2, n - 1, 2)]) + f(b))/3

    return integral




def Func_interval(f, interval):
    a, b = interval

    return f(b) - f(a)



def f1(x):
  return (1/(x**2))
def f2(x): 
  return (x**2)
def f3(x): 
  return (math.sqrt(x))
def f4(x): 
  return (math.sin(x))
def f5(x): 
  return (x**3)  

funcs = [f1,f2,f3,f4,f5]


def af1(x):
  return (-1/(x))
def af2(x): 
  return ((x**3)/3)
def af3(x): 
  return ((2*x**(1.5))/3)
def af4(x): 
  return (-math.cos(x))
def af5(x): 
  return ((x**4)/4)

analitical_functions=[af1,af2,af3,af4,af5]





monte_funcs = [f1, lambda x: f1(x[0]) * f2(x[1]), lambda x: f1(x[0]) * f2(x[1]) * f3(x[2]), lambda x: f1(x[0]) * f2(x[1]) * f3(x[2]) * f4(x[3]), lambda x: f1(x[0]) * f2(x[1]) * f3(x[2]) * f4(x[3]) * f5(x[4])]



intervals = [(1, 2), (2.005, 7.095), (5, 15),(8, 10),(12, 13)]



h = 0.1
numbers = [10,100,10000]



for num in numbers:  
    quad_result = []
    monte_result = []
    analitical_result = []

    for i in range(len(intervals)):
        j = i + 1
        #print(intervals[:j])
        quad_ints = np.prod([Quadrature_method(interval, func, h) for func, interval in zip(funcs[:j], intervals[:j])])
        quad_result.append(quad_ints)

        monte_int = Monte_carlo_method(intervals[:j], monte_funcs[i], num)
        monte_result.append(monte_int)

        analitical_result.append(np.prod([Func_interval(func, interval) for func, interval in zip(analitical_functions[:j], intervals[:j])]))    
      
    print('h = ',h,'num=',num)
    print("Кратность    ", "Метод Монте-Карло", "   Метод Квадратур", "     Аналитически")
    for i in range(5):
        print('    ',i+1,'      ', monte_result[i],' ', quad_result[i],'   ', analitical_result[i])
    h=h*h    


#############################
# Второй пример 
intervals = [(0, math.pi/2), (0, math.sqrt(3))]

def f1(x):
  return int(x**0)
def f2(x): 
  return int(x**3)

funcs = [f1,f2]

monte_funcs = [f1, lambda x: f1(x[0]) * f2(x[1])]



circle_int = Monte_carlo_method(intervals[:2], monte_funcs[1], 100000)


print('С помощью метода Монте-Карло', circle_int)

int1=Quadrature_method(intervals[1], funcs[1], 0.1)
int2=Quadrature_method(intervals[0], funcs[0], 0.1)
print('С помощью квадратур', int2*int1)

# результат, полученный аналитически 
print('Вычесленный аналитически', (9*math.pi)/8)


