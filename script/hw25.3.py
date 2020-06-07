
import numpy as np
import matplotlib.pyplot as plt

t = np.array([],dtype = np.float64)
y1 = np.array([],dtype = np.float64)
z1 = np.array([],dtype = np.float64)
y2 = np.array([],dtype = np.float64)
z2 = np.array([],dtype = np.float64)

t = np.append(t,0)
y1 = np.append(y1,2)
z1 = np.append(z1,0)
y2 = np.append(y2,2)
z2 = np.append(z2,0)
h = 0.1

for i in range(40):
  #Euler Method
  t = np.append(t,h*(i+1))
  y1 = np.append(y1,y1[i]+h*z1[i])
  z1 = np.append(z1,z1[i]+h*(t[i]-y1[i]))
  #Heun's Method
  y2_next = y2[i] + z2[i] * h #guess next y
  z2 = np.append(z2,z2[i]+h*(t[i]-y2[i]+t[i+1]-y2_next)/2) #get next y' use guessed y
  y2 = np.append(y2,y2[i]+h*(z2[i]+z2[i+1])/2)

plt.plot(t,y1,label='Euler')
plt.plot(t,y2,label='Heun')
plt.legend()
plt.show()

print(y2[0:5])
