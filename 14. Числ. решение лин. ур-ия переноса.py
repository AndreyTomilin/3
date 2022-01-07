# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

#Уравнение:
# du/dt + c*du/dx = f(x,t)

#c -скорость звука в среде
c = 300

#начальное условие u0(x)
def u0(x):
    return 0


#краевое условие phi(t)
def phi(t):
    return 1

#пространственный интервал: 0 <= x <= l
l = 2
#число точек разбиения пространственного интервала
N = 50
#пространственный шаг сетки
h = (l-0) / N

#временной интервал (время расчета)
T = 8*l/c
#временной шаг сетки
dt = 1/c * 0.8 *h
#число точек разбиения временного интервала
Nt = int(T/dt)
print('Nt=',Nt)

#число Куранта
r = c*dt/h


#интервал положения источника (alfa,betha) < l
alfa = 0.5
betha = 0.9

#источник-сток вещества
def f(x,t):
    if (alfa <= x <= betha):
        return 0
    else:
        return 0

x = []
u_0 = []
#начальное условие
for i in range(0,N+1):
    x.append(0+h*i)    
    u_0.append(u0(x[i]))

u = [0]*(N+1)
for m in range(0,Nt):
    t = m*dt #время на текущем шаге
    u[0] = phi(t) #значение на левом конце интервала (из краевого условия)
    #отображаем краевое условие в начальный момент времени    
    if m == 0:
        plt.plot(x,u,label='t0')
#========================================================================
    for i in range(1,N+1):
        u[i] = 1/(1+r) *(u[i] + r*u[i-1] +dt*f(x[i]-h/2,t+dt/2))
#========================================================================
    if m == 10:#int(Nt/5):
        plt.plot(x,u, label='t='+str(t))
    if m == 30:
        plt.plot(x,u,label='t='+str(t))
    if m == 50:
        plt.plot(x,u,label='t='+str(t))
    if m == 70:
        plt.plot(x,u,label='t='+str(t))
    if m == 90:
        plt.plot(x,u,label='t='+str(t))
plt.legend()
