

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,4,8,9])
y = np.array([5,4,6,7,8])

c0 = np.sum(x**0)
c1 = np.sum(x**1)
c2 = np.sum(x**2)
b0 = np.sum(y)
b1 = np.sum(y*x)

c = [[c0,c1],
     [c1,c2],
     ]
b = [b0,b1]

a = np.linalg.solve(c,b)

def P(x):
    return a[0] + a[1]*x
 

x_new = np.linspace(min(x), max(x), 100)

plt.plot(x,y,'o')
plt.plot(x_new,P(x_new))