# -*- coding: utf-8 -*-
from math import *
import matplotlib.pyplot as plt

N = 20
a = -2
b = 2
h = (b-a)/N

def f(x):
    return x**2-1


x=[]
y=[]
for i in range(N+1):
    x.append(a+i*h)
    y.append(f(x[i]))
    
plt.plot(x,y,'-')
plt.grid(True)
plt.show()

eps = 0.01
#начальное приближение
x_cur = 0.1
x_old = 0.2
k = 0
k_max = 100
for i in range(0,k_max):
    x_new = x_cur - (x_cur-x_old) / (f(x_cur) - f(x_old)) * f(x_cur)
    print('xnew=',x_new)
    k = k + 1
    if abs(x_new-x_cur) < eps:
        break
    x_old = x_cur
    x_cur = x_new

print(x_new)
print(k)

