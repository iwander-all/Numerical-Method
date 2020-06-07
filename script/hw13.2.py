import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)   
y = -1.5*x*x*x*x*x*x-2*x*x*x*x+12*x
plt.plot(x,y)
plt.grid()
plt.show()


xi = 2.25
xi_1 = 1.5

for i in range(4):
	print(i)
	yi = math.sin(xi) + math.cos(1 + xi*xi) - 1
	print("yi:",yi)
	yi_1 = math.sin(xi_1) + math.cos(1 + xi_1*xi_1) - 1
	print("yi_1:",yi_1)
	xiplus1 = xi - yi * (xi_1-xi) / (yi_1-yi)
	print("xiplus1:",xiplus1)	
	xi_1 = xi
	xi = xiplus1

print(xiplus1)


