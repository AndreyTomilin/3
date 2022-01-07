# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

n = 3
p = 3
q = 2
b = 0.05
eps = 0.001
k_max = 100

a = np.zeros((n,n))
X_0 = np.random.random(n)

for i in range(n):
    for j in range(n):    
        if (i == j):
            a[i][j] = i+1#5*(i+1)**(p/2)
        if (i != j):
            a[i][j] = 0#b * ( (i+1)**(p/2) + (j+1)**(p/2) )**(1/q)
   

k = 1

X_old = X_0
lambda_old = 0
while (k < k_max):
    k += 1
    norm_X_old = np.sqrt(np.vdot(X_old,X_old))
    e_old = X_old / norm_X_old
    X_new = np.dot(a,e_old)
    lambda_new = np.dot(X_new, e_old)
    if (abs(lambda_new - lambda_old) <= eps):
        break
    X_old = X_new
    lambda_old = lambda_new

print('lambda = ',lambda_new)
print('X = ', X_new)  
print('k = ',k)

print(a[0])
print(a[1])
print(a[2])
#print(a[3])
#print(a[4])


