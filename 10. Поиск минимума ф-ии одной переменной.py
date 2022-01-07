# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

a = -1
b = 5
c = 2 / (3 + sqrt(5))
eps = 0.001
n = 50
k_max = 50

def f(x):
    return (x-3)**2

x = np.linspace(a,b,n)
y = f(x)
plt.plot(x,y)
plt.show()

l = []
k_array = []
delta = []
for k in range(k_max+1):
    if abs(a-b) <= 2*eps: break
    x1 = a + c*(b-a)
    x2 = a + (1-c)*(b-a)
    if (f(x1) > f(x2)):
        a = x1
    else:
        b = x2
    k_array.append(k)
    l.append(0.5*(b-a))
    delta.append(-log(l[k],10))

print('k=',k)
print('a=',a,'f(a)=',f(a))
print('b=',b, 'f(b)=',f(b))

#plt.subplot(121)
plt.plot(x,y)
"""plt.xlabel('k')
plt.legend([r'$l(k)$'])
plt.subplot(122)
plt.plot(k_array,delta)
plt.legend([r'$\delta(k)$'])
plt.xlabel('k')"""
plt.show()
        



