import math
import numpy as np
import matplotlib.pyplot as plt

t = np.array([],dtype = np.float64)
y = np.array([],dtype = np.float64)
t = np.append(t,0)
y = np.append(y,0)
h = 0.1

for i in range(20):
  t = np.append(t,h*(i+1))
  y = np.append(y,(y[i]+99999*math.exp(-t[i+1])*h)/(1+100000*h))

plt.plot(t,y,label='implicit')
plt.legend()
plt.show()

print(t)
print(y)
