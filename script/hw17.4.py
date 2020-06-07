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

#question 1
x = np.array([6,7,11,15,17,21,23,29,29,37,39],dtype = np.float64)
y = np.array([29,21,29,14,21,15,7,7,13,0,3],dtype = np.float64)
a0,a1 = calLine(x,y)
print("y = %f x + %f"%(a1,a0))
plt.scatter(x,y)
x = np.linspace(0, 50, 1000) 
y = a1*x + a0
plt.plot(x,y)
plt.show()

#question 2
x = np.array([6,7,11,15,17,21,23,29,29,37,39,10],dtype = np.float64)
y = np.array([29,21,29,14,21,15,7,7,13,0,3,10],dtype = np.float64)
a0,a1 = calLine(x,y)
n = x.shape[0]
Sr = (y-a0-a1*x) * (y-a0-a1*x)
Sr_sum = Sr.sum()
S_xy = math.sqrt(Sr_sum/(n-2))

St = (y-y.sum()/n) * (y-y.sum()/n)
St_sum = St.sum()
Sy = math.sqrt(St_sum/(n-1))

print("St=%f, Sr=%f" % (St_sum,Sr_sum))
print("Sy=%f, Sy/x=%f" % (Sy,S_xy))
