# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:24:53 2016
"""
from math import *
import matplotlib.pyplot as plt

N = 100
a = 0
b = 1
h = (b-a) / N

def u(x):
    return x*(1-x) - 1/8

x=[]
f=[]
for i in range(N+1):
    x.append(a+i*h)
    f.append(u(x[i]))
    
plt.plot(x,f,'-')
plt.show()

f_max = f[0]
i_max = 0
f_min = f[0]
i_min = 0
f_avr = 0
f_avr_square = 0
f_plus = 0
f_minus = 0
for i in range(N+1):
    if (f[i] > f_max):
        f_max = f[i]
        i_max = i
    if (f[i] < f_min):
        f_min = f[i]
        i_min = i
    f_avr = f_avr + f[i]
    f_avr_square = f_avr_square + f[i]**2
    if (f[i] > 0):
        f_plus += 1
    if (f[i] < 0):
        f_minus += 1
    
f_avr = 1/(N+1) * f_avr
f_avr_square = 1/(N+1) * f_avr_square
f_plus = f_plus / (N+1)
f_minus = f_minus / (N+1)

sigma = 0
for i in range(N+1):
    sigma = sigma + (f[i] - f_avr)**2
sigma = sqrt(sigma / (N+1))
print('f_max = ', f_max, 'i_max= ', i_max)
print('f_min = ', f_min, 'i_min =', i_min)
print('f_avr = ', f_avr)
print('f_avr_square = ', f_avr_square)
print('f_avr_square_root = ', sqrt(f_avr_square))
print('f_plus = ', f_plus)
print('f_minus = ', f_minus)
print('sigma =', sigma)