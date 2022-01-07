# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

n = 5
p = 3
q = 2

a = np.zeros((n,n+1))
l = np.zeros((n,n+1))
u = np.zeros((n,n+1))

for i in range(n):
    for j in range(n+1):    
        if (i == j and j != n):
            a[i][j] = 5*(i+1)**(p/2)
        if (i != j and j != n):
            a[i][j] = (-1)**(i+1)*(j+1) * 0.01* ((i+1)**(p/2) + (-1)**(i+1)*(j+1)*(j+1)**(q/2))
        if (j == n):
            a[i][j] = 4.5*(i+1)**(p/2)

#заполняем матрицу L
for j in range(n):
    for m in range(j,n):
        l[m][j] = 1
     

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])


