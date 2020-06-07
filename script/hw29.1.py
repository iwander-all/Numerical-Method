import math
import numpy as np
import matplotlib.pyplot as plt

T = np.array([[0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 50.],
              [0., 0., 0., 0., 50.],
              [0., 0., 0., 0., 50.],
              [150.,150.,150.,150.,150.,]],dtype = np.float64)
e = 0.
e_prev = 1.
relax = 1.2

while (e_prev > 0.01):
  for i in range(1,4):
    for j in range(4):
      prev = T[i,j]
      if (j == 0):
        T[i,j] = (2*T[i,j+1] + T[i-1,j] + T[i+1,j]) / 4
      else:
        T[i,j] = (T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1]) / 4
        T[i,j] = relax * T[i,j] + (1-relax) * prev
      if (T[i,j] > 0):
        e_temp = abs(T[i,j] - prev) / T[i,j]
      else:
        e_temp = 1.
      if (e < e_temp):
        e = e_temp
  e_prev = e
  e = 0.  
    
print(T[1:4,1:4])
