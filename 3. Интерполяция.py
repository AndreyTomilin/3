# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

a = 1
b = 5
N = 20
h = (b-a)/N

def f(x):
    return x**2 #x**3/(a + b*x)**5

#исходные точки данных
x = []
y = []
for j in range(N+1):
    x.append(a+j*h)
    y.append(f(x[j]))

#первые разности
y1 = []
for j in range(N):
    y1.append( (y[j+1]-y[j]) / h)
#вторые разности
y2=[]
for j in range(N-1):
    y2.append( (y[j+2]-2*y[j+1]+y[j]) / (2*h**2))

#полином Ньютона, зависит от исходных точек данных, вычисляет значение
#в новой точке x_arg
def P(x_arg,j):
    return y[j] + (x_arg-x[j])*y1[j] + (x_arg-x[j])*(x_arg-x[j+1])*y2[j]

x_new = []
y_new = []
eps = []
eps_max = 0
for j in range(N-1):
    x_new.append(a+(j+1/2)*h)
    y_new.append(P(x_new[j],j))
    eps.append( abs(f(x_new[j]) - P(x_new[j],j)) )
    if abs(eps[j]) > eps_max:
        eps_max = eps[j]
#средний квадрат погрешности
eps_square = 0
for j in range(N-1):
    eps_square = eps_square + eps[j]**2
eps_square = eps_square / (N-1)
  
plt.subplot(211)
plt.plot(x,y,'o',x_new,y_new,'-')
plt.subplot(212)
plt.plot(x_new,eps,'o')
plt.show()
print('eps_max = ', eps_max)
print('eps_square = ', eps_square)
print('eps_square_root = ', sqrt(eps_square))
