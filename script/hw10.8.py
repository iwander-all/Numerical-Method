import math
import numpy as np
from numpy.linalg import*
import matplotlib.pyplot as plt

import scipy as scipy
from scipy import linalg

A = np.array([[15,-3,-1],[-3,18,-6],[-4,-1,12]],np.float64)
b = np.array([[2600],[850],[2400]],np.float64)


l,u = scipy.linalg.lu(A,True)

print('L,U = ',l,u)
print('L * U = ',(l * u)) # equivalent to A.LUsolve(b)
#x = A.solve(b)
#print('x = ',x)

A_1 = np.linalg.inv(A)
print('A-1:',A_1)

x = A_1 * b
print(x)
