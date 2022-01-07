# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

a = 0
b = 1
N = 20
h = (b-a)/N

def f(x):
    return x**2

x = []
y = []
for j in range(N+1):
    x.append(a+h*j)
    y.append(f(x[j]))

x_center = []
y_center = []
for j in range(N):
    x_center.append(a+(j+1/2)*h)
    y_center.append(f(x_center[j]))

I_rect = 0
for j in range(N):
    I_rect = I_rect + y_center[j]
I_rect = I_rect * h

m = 5
A = [0]*(m+1)
t = [0]*(m+1)
A[1] = 0.118463443
A[5] = A[1]
A[2] =  0.239314335
A[4] = A[2]
A[3] = 0.284444444
t[1] = 0.046910077
t[2] = 0.230765345
t[3] = 0.5
t[4] = 1 - t[2]
t[5] = 1 - t[1]
I_quad = 0
for j in range(1,m+1):  
    I_quad = I_quad + A[j]*f(a+(b-a)*t[j])
I_quad = I_quad*(b-a)
  
plt.subplot(211)
plt.plot(x,y,'o',x_center,y_center,'x')

print('I_rect = ', I_rect)
print('I_quad = ', I_quad)
