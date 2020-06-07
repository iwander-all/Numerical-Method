
import numpy as np
import matplotlib.pyplot as plt

t = np.array([],dtype = np.float64)
y = np.array([],dtype = np.float64)


t = np.append(t,0)
y = np.append(y,1)

h = 0.5

for i in range(6):
  t = np.append(t,h*(i+1))
  k1 = -y[i] + t[i]*t[i]
  k2 = -(y[i]+k1/2) + (t[i]+h/2)*(t[i]+h/2)
  k3 = -(y[i]-k1+2*k2) + (t[i]+h)*(t[i]+h)
  y = np.append(y,y[i]+(k1 + 4*k2 +k3)/6)

plt.plot(t,y,label='3th RK')
plt.legend()
plt.show()

print(t)
print(y)
