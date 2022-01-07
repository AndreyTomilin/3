# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

beta = 0.8
alpha = sqrt(1-beta**2)
a,b = 1, 1
m, n = 4, 4
d = sqrt(a**2+b**2)
eps = 0.001
k_max = 1000
X_0 = d
Y_0 = d

def f(x,y):
    return ((alpha*x-beta*y)/a)**m + ((alpha*y+beta*x)/b)**n

#минимум ф-ии одной переменной
def argmin(f,a,b,eps):
    c = 2 / (3 + sqrt(5))
    for k in range(k_max+1):
        if abs(a-b) <= 2*eps: break
        x1 = a + c*(b-a)
        x2 = a + (1-c)*(b-a)
        if (f(x1) > f(x2)):
            a = x1
        else:
            b = x2
    return (a+b)/2

fig = plt.figure(1) 		
ax = fig.gca(projection='3d') 
X = np.linspace(-d, d, 100) 	
Y = np.linspace(-d, d, 100) 
X, Y = np.meshgrid(X, Y) 	
Z = f(X,Y)
surf = ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.cm.rainbow)
fig.colorbar(surf)
plt.show()

X_old = X_0
Y_old = Y_0
k_array = []
q = []
for k in range(k_max+1):
    #определяем ф-ию одной переменной при фиксированном y    
    def f_x(x): return f(x,Y_old)    
    X_new = argmin(f_x,-d,d,eps)
    #определяем ф-ию одной переменной при фиксированном x    
    def f_y(y): return f(X_new,y)
    Y_new = argmin(f_y,-d,d,eps)
    delta = sqrt((X_new-X_old)**2 + (Y_new-Y_old)**2)
    k_array.append(k)
    q.append(log(delta+0.0000000000000001)/log(10))
    if (delta <= eps):
        break
    X_old = X_new
    Y_old = Y_new

print('X_min = ', X_new)
print('Y_min = ', Y_new)
print('f_min = ', f(X_new,Y_new))
print('k = ', k)

plt.plot(k_array,q,'-')
plt.show()
        
