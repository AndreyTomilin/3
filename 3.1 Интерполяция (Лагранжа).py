# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

X=[1,2,4,8,9]
Y=[5,4,6,7,8]
n = len(X)

def L(x):
    S = 0 #сумма    
    for i in range(n):
        P=1 #произведение        
        for j in range(n):
            if i != j:
                P = P * (x-X[j]) / (X[i]-X[j])
        S = S + Y[i] * P
    return S


plt.plot(X,Y,'o')
plt.grid(True)
plt.show()

#исходных точек 10, строим новый график в 100 точках
M = 100
A = min(X)
B = max(X)
h = (B-A) / M
xnew = [A+i*h for i in range(M+1)]
ynew=[L(x) for x in xnew]
plt.plot(xnew,ynew,'-')