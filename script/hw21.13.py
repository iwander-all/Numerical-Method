import math
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,0.05,0.15,0.25,0.35,0.475,0.6],dtype = np.float64)
y = np.array([2,1.8555,1.5970,1.3746,1.1831,0.9808,0.8131],dtype = np.float64)

plt.plot(x,y)
plt.plot(x,y,'o')
plt.show()
true_I = -2/1.5 * (math.exp(-1.5*0.6) - 1)
print("true integral from a = 0 to b = 0.6:%f"%true_I)

#(a)
mean = np.mean(x)
mean_I = mean * 0.6
print("(a) the integral from a = 0 to b = 0.6 using analytical means:%f"%mean_I)

#(b)
trapezoidal_I = 0.
for i in range(6):
	trapezoidal_I = trapezoidal_I + (x[i+1]-x[i])*(y[i+1]+y[i])/2.
print("(b) the integral from a = 0 to b = 0.6 using trapezoidal rule:%f"%trapezoidal_I)

#(c)
combine_I = 0
for i in range(4):
	combine_I = combine_I+ (x[i+1]-x[i])*(y[i+1]+y[i])/2
combine_I += (x[6]-x[4])*(y[4]+y[6]+4*y[5])/6
print("(c) the integral from a = 0 to b = 0.6 using combined rule:%f"%combine_I)
#(d)
print("error in (b):%f"%(abs(true_I-trapezoidal_I)/true_I))
print("error in (c):%f"%(abs(true_I-combine_I)/combine_I))
