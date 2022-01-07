# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt

#Уравнение:
# du/dt = a^2*d2u/dx2 + f(x,t)

#a температуропроводность
a = 1

#пространственный интервал: 0 <= x <= l
l = 2
#число точек разбиения пространственного интервала
N = 50
#пространственный шаг сетки
h = (l-0) / N

#временной интервал (время расчета)
T = 1
#временной шаг сетки
dt = 0.5 * h/a**2
print('dt=',dt)
#число точек разбиения временного интервала
Nt = int(T/dt)
print('Nt=',Nt)

#константы расчета
mu = 2*h**2 / (dt*a**2)
sigma = 2 + mu
nu = 2*h**2 / a**2
teta = 2 - mu

#начальное условие u0(x)
def u0(x):
    return x/l

#краевое условие на левой границе
def phi1(t):
    return 1

#краевое условие на правой границе
def phi2(t):
    return 0

#источник-сток тепла
def f(x,t):
    return 0

x = []
u_old = []
u_anal = []
#начальное условие
for j in range(0,N+1):
    x.append(0+h*j)    
    u_old.append(u0(x[j]))
    u_anal.append(1-x[j]/l)
#отображаем краевое условие в начальный момент времени    
plt.plot(x,u_old,label='t0')

g = [0]*(N+1)
Xi = [0]*(N+1)
Eta = [0]*(N+1)
u_new = [0]*(N+1)
#===========================================================================
#основной цикл по времени с 1 т.к. при t=0 решение уже известно - u_old=u0(x)
for m in range(1,Nt):
    t = m*dt #время на текущем шаге

    #вычисляем g[j]    
    for j in range(1,N):
        g[j] = -nu*f(x[j],t+dt/2) - (u_old[j+1] - teta*u_old[j] + u_old[j-1])

    #прямой ход прогонки
    Xi[1] = 0
    Eta[1] = phi1(t)
    for j in range(1,N):
        Xi[j+1] = 1/(sigma-Xi[j])
        Eta[j+1] = (Eta[j]-g[j])*Xi[j+1]
        
    #обратный ход прогонки (в методичке должно быть j=N-1...0)
    u_new[N] = phi2(t)
    for j in range(N-1,-1,-1):
        u_new[j] = Xi[j+1]*u_new[j+1] + Eta[j+1]
    
    u_old[:] = u_new[:]
    if m == 1:
        plt.plot(x,u_new, label='t='+str(t))
    if m == 10:
        plt.plot(x,u_new,label='t='+str(t))
    if m == 20:
        plt.plot(x,u_new,label='t='+str(t))
    if m == 50:
        plt.plot(x,u_new,label='t='+str(t))
#============================================================================
        
#аналитическое решение
plt.plot(x,u_anal, 'y--', label='u_anal')
plt.legend()
print('u(0)=',u_new[0])
print('u(N)=',u_new[N])