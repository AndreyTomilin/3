# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt


omega0 = 1.5
betha = 0.1


#начальные условия
Q0 = 5
I0 = 0


#время расчета
N = 50
dt = 0.05*2*pi/omega0


def E(Q,I,t):
    return (1+1*abs(Q)**1+1*abs(I)**1) * t**0.1 * sin(2*t+pi/2)

Q=[]
I=[]
time=[]
Q.append(Q0)
I.append(I0)
time.append(0)

for i in range(0,N):
    Q1 = Q[i] + dt/2 * I[i]
    I1 = I[i] + dt/2 * (-2*betha*I[i]-omega0**2*Q[i] + E(Q[i],I[i],time[i]+dt/2))
       
    Q.append(Q[i]+I1*dt)
    I.append(I[i]+(-2*betha*I1-omega0**2*Q1 + E(Q1,I1,time[i]+dt/2))*dt)
    
    time.append((i+1)*dt)

plt.subplot(311)
plt.plot(time,Q,'-')
plt.title('Q(t)')
plt.subplot(312)
plt.plot(time,I,'-')
plt.title('I(t)')
plt.subplot(313)
plt.plot(Q,I,'-')
plt.title('Q(I)')
plt.show()
    
