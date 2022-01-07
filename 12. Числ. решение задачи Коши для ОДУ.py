# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt


q = 1.6e-19
m0 = 9.1e-31
c = 300e+6

#начальные условия
x0 = 0
V0 = 0.7e+6
gamma = 1 / sqrt(1-(V0/c)**2)
p0 = gamma * m0 *V0

#время расчета
N = 100
dt = 10e-10
T = N*dt 

#потенциал:
def fi(x):
    return 500*x**2(1+2*x**3)**2
#поле
def E(x):
    return 1000*x*(2*x**3+1)**2+6000*x**4*(2*x**3+1)
    
x=[]
p=[]
time=[]
x.append(x0)
p.append(p0)
time.append(0)

for i in range(0,N):
    time.append((i+1)*dt)
    x1 = x[i] + dt/2 * p[i]/(gamma*m0)
    p1 = p[i] + dt/2 *q*E(x[i])
    
    gamma = sqrt(1+(p1/(m0*c))**2)
    
    x.append(x[i]+p1/(gamma*m0)*dt)
    p.append(p[i]+q*E(x1)*dt)

plt.subplot(311)
plt.plot(time,x,'-')
plt.title('x(t)')
plt.subplot(312)
plt.plot(time,p,'-')
plt.title('p(t)')
plt.subplot(313)
plt.plot(x,p,'-')
plt.title('x(p)')
plt.show()
        
