# -*- coding: utf-8 -*-
from math import *
import matplotlib.pyplot as plt
from scipy.misc import derivative

N = 20
a = -2
b = 2
h = (b-a)/N

def f(x):
    return x**3


x=[]
y=[]
for i in range(N+1):
    x.append(a+i*h)
    y.append(f(x[i]))
    
plt.plot(x,y,'-')
plt.grid(True)
plt.show()

eps = 0.00001
#начальное приближение
x_old = 0.1
k = 0
k_max = 1000
for i in range(0,k_max):
    x_new = x_old - f(x_old) / derivative(f,x_old)
    k = k + 1
    if abs(x_new-x_old) < eps:
        break
    x_old = x_new

print(x_new)
print(k)

