# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

n = 5
p = 3
q = 2
b = 0.05
eps = 0.001
k_max = 100

def f(i,j):
    if (i == j):
        return 5*(i+1)**(p/2)
    else:
        return b * ( (i+1)**(p/2) + (j+1)**(p/2) )**(1/q)

a = np.zeros((n,n)) #np.fromfunction(f,(n,n))
X_0 = np.random.random(n)

for i in range(n):
    for j in range(n):    
        a[i,j] = f(i,j)
print(a)

k = 0

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


