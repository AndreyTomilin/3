
import numpy as np

A = [[10,1,1],
     [2,20,2],
     [3,3,30]]
b = [1,2,3]
n = len(b)
eps = 0.01

x_old = [0,0,0]
x_new = [0,0,0]
err = [np.inf,np.inf,np.inf]

while max(err) > eps:
    for i in range(n):
        S = 0
        for j in range(n):
            if j != i:
                S = S + A[i][j]*x_old[j]
        
        x_new[i] = 1/A[i][i] * (b[i] - S)
        
        err[i] = abs(x_new[i] - x_old[i])
        x_old[i] = x_new[i]

print('Якоби:', x_new)
print('Scipy:', np.linalg.solve(A,b))


