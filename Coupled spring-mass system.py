# -*- coding: utf-8 -*-


from scipy.integrate import odeint
import matplotlib.pyplot as plt

#right hand system
def D(arg, t, par):
    """
    Arguments:
        arg :  vector of the state variables:
                  arg = [x1,y1,x2,y2]
        t :  time
        par :  vector of the parameters:
                  p = [m1,m2,k1,k2,L1,L2,b1,b2]
    """
    x1, y1, x2, y2 = arg
    m1, m2, k1, k2, L1, L2, b1, b2 = par

    # Create f = (x1',y1',x2',y2'):
    f = [
        y1,
        (-b1*y1 - k1*(x1-L1) + k2*(x2-x1-L2)) / m1,
        y2,
        (-b2*y2 - k2*(x2-x1-L2)) / m2
        ]
    return f

# Masses:
m1 = 1.0
m2 = 1.5
# Spring constants
k1 = 8.0
k2 = 40.0
# lengths
L1 = 0.5
L2 = 1.0
# Friction coefficients
b1 = 0.8
b2 = 0.5

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1 = 0.5
y1 = 0.0
x2 = 2.25
y2 = 0.0

# ODE solver parameters
endTime = 15.0
N = 250
#time
t = [endTime*i/N for i in range(N+1)]

# Pack up the parameters and initial conditions:
p = [m1, m2, k1, k2, L1, L2, b1, b2]
u0 = [x1, y1, x2, y2]

# Call the ODE solver.
u = odeint(D, u0, t, (p,))

#координаты первого и второго грузика
plt.plot(t,u[:,0],t,u[:,2])
plt.show()

