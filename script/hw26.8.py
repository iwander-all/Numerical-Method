import math
import numpy as np
import matplotlib.pyplot as plt

t = np.array([],dtype = np.float64)
y = np.array([],dtype = np.float64)
t = np.append(t,0)
y = np.append(y,2)
h = 0.5

#get y at t = 0.5, 1, 1.5 using Euler
for i in range(3):
  t = np.append(t,h*(i+1))
  y = np.append(y,(y[i]+(-2*y[i])/(1+t[i])))

#get y at t = 2, 2.5 using Adams
for i in range(3,5):
  t = np.append(t,h*(i+1))  
  #use Open formulas to predict
  y_predict = y[i] + h * ((-2*y[i])/(1+t[i]) * 55./24 -
                          (-2*y[i-1])/(1+t[i-1]) * 59./24 +
                          (-2*y[i-2])/(1+t[i-2]) * 37./24 -
                          (-2*y[i-3])/(1+t[i-3]) * 9./24)
  y = np.append(y,y_predict)
  #use close formulas to correct
  for j in range(6):
    y_correct = y[i] + h * ((-2*y[i+1])/(1+t[i+1]) * 9./24 -
                            (-2*y[i])/(1+t[i]) * 19./24 -
                            (-2*y[i-1])/(1+t[i-1]) * 5./24 +
                            (-2*y[i-2])/(1+t[i-2]) * 1./24) 
    y[i+1] = y_correct

plt.plot(t,y,label='Adams Method')
plt.legend()
plt.show()

print(t)
print(y)
