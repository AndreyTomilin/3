# -*- coding: utf-8 -*-
from math import *
import matplotlib.pyplot as plt

N = 20
a = 2
b = 4
h = (b-a)/N

def f(x):
    return sin(x)

x=[]
y=[]
for i in range(N+1):
    x.append(a+i*h)
    y.append(f(x[i]))
    
plt.plot(x,y,'-')
plt.grid(True)
plt.show()


eps = 0.001
k = 0
while abs(b-a) >= 2*eps:
    k = k +1    
    x0 = (a + b) / 2
    if (f(a)*f(x0) <= 0):
        b = x0
    else:
        a = x0
print((a+b)/2)
print('k=',k)

