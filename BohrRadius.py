from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform

# Set common figure parameters:
newparams = {'axes.titlesize': 7, 'axes.labelsize': 6, 'axes.linewidth': 1, 'savefig.dpi': 300, 
             'lines.linewidth': 1.0, 'lines.markersize': 2.4, 'figure.figsize': (3, 3), 'figure.subplot.wspace': 0.4,
             'ytick.labelsize': 6, 'xtick.labelsize': 6, 'ytick.major.pad': 3, 'xtick.major.pad': 3,
             'xtick.major.size': 2, 'ytick.major.size': 2, 'legend.handlelength': 1.5, 'figure.dpi': 200}
plt.rcParams.update(newparams)

#Plot circle
x = lambda theta: np.cos(theta)
y = lambda theta: np.sin(theta)
theta = np.linspace(0, 2*np.pi, 2000)
plt.plot(x(theta), y(theta), 'r')

#Plot square
plt.plot([-1,1],[-1,-1],'b',[-1,1],[1,1],'b',[-1,-1],[-1,1],'b',[1,1],[-1,1],'b')
plt.xlim([-1.1, 1.1])
plt.ylim([-1.1, 1.1])

#Generate two sets of 10 random numbers
x = uniform(-1, 1, 10)
y = uniform(-1, 1, 10)
plt.plot(x, y, '*k', lw=0.1)
plt.show()

#Setting up the Monte Carlo Integral methods 
N = 1000000
V = 4
i = 0
n = 0
while i < N:                              #Takes random numbers and takes the average 
    x = uniform(-1, 1)                    
    y = uniform(-1, 1)
    r = np.sqrt(x**2+y**2)
    if r <= 1:
        n = n + r
    i = i + 1
    
I = V/N*n                                 
print(r'Monte Carlo integral: %f' % I)
print(r'Analytical integral: %f' % (2/3*np.pi))

N = 1000000     # Number of random numbers
a = 0.529e-10   # Bohr radius
i = 0
n = 0.0
j = 1.0         # number of Bohr radii to integrate over
while i < N:    # Monte Carlo integration for and electron in a sphere with r = a
    x = uniform(-j*a, j*a)
    y = uniform(-j*a, j*a)
    z = uniform(-j*a, j*a)
    r = np.sqrt(x**2 + y**2 + z**2)
    if r <= j*a:
        n = n + np.exp(-2*r/a)/(np.pi*a**3)
        
        
    i = i + 1
    
prob = n/N*(2*j*a)**3

print(r'The probability within one Bohr radius is: %s' % prob)
probAnalytical = 1-np.exp(-2*j)*(1+2*j+2*j**2)
print(r'The analytical probability is: %s' % probAnalytical)

#plotting the probabilty density in the x-y plane
p = 1000
xs = np.linspace(-j*a, j*a, p, True)
X,Y = np.meshgrid(xs, xs)
psi2 = np.zeros([p, p])

r = np.sqrt(X**2+Y**2)

psi2 = np.exp(-2*r/a)/(np.pi*a**3)

plt.figure(figsize=(5,4))
levels = np.linspace(0, 1, 200, True)
C = plt.contourf(X/a, Y/a, psi2*(np.pi*a**3), levels)
plt.title(r'Probability density for 1s state')
plt.ylabel(r'$y/a$')
plt.xlabel(r'$x/a$')
cbar = plt.colorbar(C)
cbar.ax.set_ylabel(r'Probability density (relative maximum)')
plt.show()
