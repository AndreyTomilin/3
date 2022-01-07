# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

L = 3
N = [100, 10000, 100000]

def ro(x1,x2,x3):
    alfa1 = -5
    alfa2 = 1
    alfa3 = 5
    beta1 = 0.5
    beta2 = 2
    beta3 = 3
    #return (abs(x1-3)**0.5)+(fabs(x2-4)**2)+(abs(x3+2)**3)
    return (abs(x1-2)**0.5)*(abs(x2-3)**2)*(abs(x3+1)**3)  
    #return abs(x1-alfa1)**beta1 + abs(x2-alfa2)**beta2 + abs(x3-alfa3)**beta3
    #return (abs(x1-2)**0.5)+(abs(x2-2)**2)+(abs(x3+1)**3)
    #return (math.e**(0.2*(math.fabs(x1+1)**0.1))*math.e**(0.4*(math.fabs(x2)**1))*math.e**(0.5*(math.fabs(x3-1)**2)))

c1, c2, c3 = 1, 3, 2
a_x, a_y, a_z = -c1,-c2,-c3
b_x, b_y, b_z = c1, c2, c3
#объем параллелепипеда
W = (b_x-a_x) * (b_y-a_y) * (b_z-a_z)
print(W)


# Set spherical angles:
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = numpy.meshgrid(theta, phi)

x = c1 * numpy.sin(theta) * numpy.cos(phi)
y = c2 * numpy.sin(theta) * numpy.sin(phi)
z = c3 * numpy.cos(theta)

fig = plt.figure(1) 
ax = fig.gca(projection='3d')
ax.plot_wireframe(x, y, z,  rstride=10, cstride=10, color='b')
plt.show()



for l in range(0,L):
    M = 0
    S = 0    
    for j in range(0,N[l]+1):
        #генерируем случайным образом координаты точки в области определения (параллелепипед)        
        Xi_x = a_x + (b_x-a_x) * np.random.random()
        Xi_y = a_y + (b_y-a_y) * np.random.random()
        Xi_z = a_z + (b_z-a_z) * np.random.random()
        #если координаты точки (Xi_x, Xi_y, Xi_z) внутри эллипсоида
        if (Xi_x**2 / c1**2 + Xi_y**2 / c2**2 + Xi_z**2 / c3**2 <= 1):
            M = M + 1
            S = S + ro(Xi_x,Xi_y,Xi_z)
    V = M * W / N[l]
    I = W * S / N[l]
    print("="*80)    
    print("Общее цисло точек (N):", N[l])
    print("Число точек внутри области (M):", M)
    print("Объем области (V):", V)
    print("Значение интеграла (I):", I)
    print("="*80)
    print()

print("Объем эллипсоида аналит. (V)", 4/3*np.pi*c1*c2*c3)






