# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

N = 40
h = 1/N

def f(x):
    return x**4/4

def df_anal(x):
    return x**3

def d2f_anal(x):
    return 3*x**2

x = []
y = []
dy_anal = []
d2y_anal = []
for j in range(N+1):
    x.append(j*h)
    y.append(f(x[j]))
    dy_anal.append(df_anal(x[j]))
    d2y_anal.append(d2f_anal(x[j]))
    

dy = [0]*(N+1)
d2y = [0]*(N+1)
eps1 = [0]*(N+1)
eps2 = [0]*(N+1)
for j in range(N+1):
    if 0 < j < N:
        dy[j] = (y[j+1] - y[j-1]) / (2*h)
        d2y[j] = (y[j+1] -2*y[j] + y[j-1]) / h**2
    if j == 0:
        dy[j] = (-3*y[0] + 4*y[1] - y[2]) / (2*h)
        d2y[j] = (12*y[0] - 30*y[1] + 24*y[2] -6*y[3]) / (6*h**2)
    if j == N:
        dy[j] = (y[N-2] -4*y[N-1] +3*y[N]) / (2*h)
        d2y[j] = (-6*y[N-3] + 24*y[N-2] -30*y[N-1] +12*y[N]) / (6*h**2)
    eps1[j] = abs(dy_anal[j] - dy[j])
    eps2[j] = abs(d2y_anal[j] - d2y[j])

eps1_max = 0
eps2_max = 0
j1_max = 0
j2_max = 0
for j in range(N+1):
    if eps1[j] > eps1_max:
        eps1_max =  eps1[j]
        j1_max = j
    if eps2[j] > eps2_max:
        eps2_max = eps2[j]
        j2_max = j

eps1_square = 0
eps2_square = 0
for j in range(N+1):
   eps1_square = eps1_square + eps1[j]**2
   eps2_square = eps2_square + eps2[j]**2
eps1_square = eps1_square / (N+1)
eps2_square = eps2_square / (N+1)

plt.subplot(311)
plt.plot(x,y,'-')
plt.title('Function')
plt.subplot(313)
plt.plot(x,d2y,'o',x,d2y_anal,'-')
plt.subplot(312)
plt.plot(x,dy,'o',x,dy_anal,'-')
plt.title('First derivative')
plt.subplot(313)
plt.plot(x,d2y,'o',x,d2y_anal,'x')
plt.title('Second derivative')
plt.ylim([0,3])
plt.show()
print('eps1_max = ', eps1_max, 'j1_max = ', j1_max)
print('eps2_max = ', eps2_max, 'j2_max=', j2_max)
print('eps1_square = ', eps1_square)
print('eps2_square = ', eps2_square)
