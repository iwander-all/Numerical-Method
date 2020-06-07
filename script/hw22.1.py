import math
import numpy as np
#from sympy import *
import sympy

x = np.array([0,0,0,0,0,0,0,0,0],dtype = np.float64)
y = np.array([0,0,0,0,0,0,0,0,0],dtype = np.float64)

h = 3. / 8
for i in range(8):
	x[i+1] = x[i] + h
	y[i+1] = x[i+1]*math.exp(x[i+1]);
print(x)
print(y)
print(" ")

I11 = (x[8]-x[0]) * (y[8]+y[0]) / 2
I12 = (x[8]-x[0]) * (y[8]+2*y[4]+y[0]) / 4
I13 = (x[8]-x[0]) * (y[8]+2*(y[2]+y[4]+y[6])+y[0]) / 8
I14 = (x[8]-x[0]) * (-y[8]+2*(y.sum())-y[0]) / 16
print("I11 = %f" %I11)
print("I12 = %f" %I12)
print("I13 = %f" %I13)
print("I14 = %f" %I14)
print(" ")

I21 = (4*I12-I11) / 3
I22 = (4*I13-I12) / 3
I23 = (4*I14-I13) / 3
print("I21 = %f" %I21)
print("I22 = %f" %I22)
print("I23 = %f" %I23)
print(" ")

I31 = (16*I22-I21) / 15
I32 = (16*I23-I22) / 15
print("I31 = %f" %I31)
print("I32 = %f" %I32)
print(" ")

I41 = (64*I32-I31) / 63
print("I41 = %f" %I41)
print(" ")

x = sympy.symbols('x')
I = sympy.integrate(x*sympy.exp(x),(x,1,3))
print("Error_a = %f" % (abs(I41-I32)/I41))
print("Error_t = %f" % (abs(I41-I)/I))

