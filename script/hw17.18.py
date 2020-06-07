import math
import numpy as np
import matplotlib.pyplot as plt

def calLine(x1,x2,y):
	n = x1.shape[0]
	x1_sum = x1.sum()
	x2_sum = x2.sum()
	y_sum = y.sum()
	x1_square = x1 * x1
	x1_square_sum = x1_square.sum()
	x1x2 = x1 * x2
	x1x2_sum = x1x2.sum()
	x1y = x1 * y
	x1y_sum = x1y.sum()
	x2_square = x2 * x2
	x2_square_sum = x2_square.sum()
	x2y = x2 * y
	x2y_sum = x2y.sum()
	Z = np.array([[n,x1_sum,x2_sum],
		      [x1_sum,x1_square_sum,x1x2_sum],
		      [x2_sum,x1x2_sum,x2_square_sum]],dtype = np.float64)
	Y = np.array([y_sum,x1y_sum,x2y_sum],dtype = np.float64)
	A = np.dot(np.linalg.inv(Z),Y)
	a2 = A[2]
	a1 = A[1]
	a0 = A[0]
	print("y = %f x1 + %f x2 + %f"%(a1,a2,a0))
	st = (y-y_sum/n) * (y-y_sum/n)
	St = st.sum()
	sr = (y-a0-a1*x1-a2*x2) * (y-a0-a1*x1-a2*x2)
	Sr = sr.sum()
	Syx = math.sqrt(Sr/(n-2))
	r = math.sqrt((St-Sr)/St)
	print("Sy/x=%f, r=%f" % (Syx,r))
	return a0,a1,a2

x1 = np.array([0,1,1,2,2,3,3,4,4],dtype = np.float64)
x2 = np.array([0,1,2,1,2,1,2,1,2],dtype = np.float64)
y = np.array([15.1,17.9,12.7,25.6,20.5,35.1,29.7,45.4,40.2],dtype = np.float64)
a0,a1,a2 = calLine(x1,x2,y)

