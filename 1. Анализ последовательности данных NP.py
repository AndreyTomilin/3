# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:24:53 2016
"""
import numpy as np
import matplotlib.pyplot as plt

N = 101
a = 0
b = 1
h = (b-a) / (N-1)
def u(i):
    x = a+i*h    
    return x*(1-x) - 1/8

x = np.linspace(a,b,N)
f = np.fromfunction(u,(N,))
plt.plot(x,f)
plt.show()

print('f_max = ', np.max(f) , 'i_max= ', np.argmax(f))
print('f_min = ', np.min(f) , 'i_min= ', np.argmin(f))
print('f_avr = ', np.sum(f)/N )
f_avr_square = f**2
print('f_avr_square = ', f_avr_square.sum()/N )
print('f_avr_square_root = ', np.sqrt(f_avr_square.sum()/N))
#argwhere() возвращает индексы массива, которые удовлетворяют условию
print('f_plus = ', len(np.argwhere(f > 0)) / N)
print('f_minus = ', len(np.argwhere(f < 0)) / N)
tmp = (f - np.sum(f)/N)**2
sigma = np.sqrt(1/N* tmp.sum())
print('sigma =', sigma)

