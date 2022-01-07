"""
Registration: xxxx; 
Description: Newton-Gregory Forward Interpolation Method 
Author: AKB
"""
import matplotlib.pyplot as plt


X=[1,2,4,8,9]
F=[5,4,6,7,8]
n = len(X)

#разделенные разности
def f(k):
    S = 0
    for j in range(k):
        P = 1
        for i in range(k):
            if i != j:
                P = P * (X[j] - X[i])
        S = S + F[j] / P
    return S

def P(x):
    S = 0
    for k in range(1,n+1):
        P = 1
        for i in range(k-1):
            P = P * (x - X[i])
        S = S + f(k) * P
    return S


plt.plot(X,F,'o')
plt.grid(True)
plt.show()

#исходных точек 10, строим новый график в 100 точках      
M = 100
A = min(X)
B = max(X)
h = (B-A) / M
xnew = [A+i*h for i in range(M+1)]
ynew=[P(x) for x in xnew]
plt.plot(xnew,ynew,'-')

