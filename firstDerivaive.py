#solves for the derivative of a function using a Pade scheme

import numpy as np
import matplotlib.pyplot as plt

#define the function you want to differentiate here
def func(x):
	return x*x*x;

a = -1.5 #left endpoint
b = 1.5 #right endpoint
N = 1000 #number of gridpoints
h = (b-a)/(N-1)

matrix = np.zeros( (N, N) )
f = np.zeros(N) #stores function values
c = np.zeros(N) #stores solution

for x in range(0, N):
	f[x] = func( x*h + a)

matrix[0,0] = 1

for x in range(1, N-1):
	matrix[x, x-1:x+2] = [1/6.0, 4/6.0, 1/6.0]

matrix[N-1,N-1] = 1

c[0] = ((-25/12.0)*f[0]
	+ 4.0*f[1]
	- 3.0*f[2]
	+ (4/3.0)*f[3]
	- (1/4.0)*f[4])/h;

c[1:N-1] = (f[2:N] - f[0:N-2])/(2*h)

c[N-1] = ((1/4.0)*f[N-5]
	-(4/3.0)*f[N-4]
	+3.0*f[N-3]
	-4.0*f[N-2]
	+(25/12.0)*f[N-1])/h;

c = np.linalg.solve(matrix, c)
X = np.linspace(a, b, N)

plt.plot(X, f, 'r', label="function")
plt.plot(X, c, 'b', label="derivative")
plt.legend()
plt.show()
