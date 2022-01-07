# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

a = 0
b = 1
N = 50
h = 1/N

def f(x):
    return exp(x**(1/2))

x = []
y = []
m1,m2,m3,m4 = 0,0,0,0
K01, K11, K21 = 0,0,0
for j in range(N+1):
    x.append(j*h)
    y.append(f(x[j]))
    m1 = m1 + x[j]
    m2 = m2 + x[j]**2
    m3 = m3 + x[j]**3
    m4 = m4 + x[j]**4
    K01 = K01 + y[j]
    K11 = K11 + x[j]*y[j]
    K21 = K21 + x[j]**2 * y[j]
m1 = m1 / (N+1)
m2 = m2 / (N+1)
m3 = m3 / (N+1)
m4 = m4 / (N+1)
K01 = K01 / (N+1)
K11 = K11 / (N+1)
K21 = K21 / (N+1)

s11 = 1
s12 = m1
s13 = m2
s22 = sqrt(m2-m1**2)
s23 = (m3-m1*m2) / s22
s33 = sqrt(m4-(s13**2+s23**2))
z1 = K01
z2 = (K11-m1*K01) / s22
z3 = (K21-(s13*z1+s23*z2)) / s33
c2 = z3/s33
c1 = (z2-s23*c2)/s22
c0 = z1 - (s12*c1 + s13*c2)

def fi(x):
    return c0 + c1*x + c2*x**2

y_new = []
eps = []
eps_max = 0
S = 0
for j in range(N+1):
    y_new.append(fi(x[j]))
    eps.append( abs(f(x[j])-fi(x[j])) )
    if eps[j] > eps_max:
        eps_max = eps[j]
    S = S + eps[j]**2
S = S / (N+1)

plt.subplot(211)
plt.plot(x,y,'o',x,y_new,'-')
plt.subplot(212)
plt.plot(x,eps,'o')
plt.show()
print('eps_max = ', eps_max)
print('S = ',S)
print('sqrt(S) = ', sqrt(S))