import math
import numpy as np
import matplotlib.pyplot as plt

def calLine(x,y):
	x_sum = x.sum()
	y_sum = y.sum()
	xy = x * y
	x2 = x * x
	x2_sum = x2.sum()
	xy_sum = xy.sum()
	n = x.shape[0]
	a1 = (n*xy_sum - x_sum*y_sum) / (n*x2_sum-x_sum*x_sum)
	a0 = y_sum/n - a1*x_sum/n
	return a0,a1

x = np.array([1,2,3,4,5],dtype = np.float64)
y = np.array([0.5,2,2.9,3.5,4],dtype = np.float64)
x = np.log(x)
print(x)
a0,a1 = calLine(x,y)
print("y = %f x + %f"%(a1,a0))
plt.scatter(x,y)
x = np.linspace(0, 50, 1000) 
y = a1*x + a0
print("a0=%f, a1=%f"%(a0,a1))
xi = np.log(2.6)
print("y=%f"%(a1*xi + a0))
plt.plot(x,y)
plt.show()

