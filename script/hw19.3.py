import math
import numpy as np
import matplotlib.pyplot as plt

t = np.array([0,2,4,5,7,8.5,12,15,20,22,24],dtype = np.float64)
pH = np.array([7.3,7,7.1,6.5,7.4,7.2,8.9,8.8,8.9,7.9,7],dtype = np.float64)
T = 24
w = 2*np.pi/T
N = t.shape[0]
A0 = pH.sum()/N
ycos = pH * np.cos(w*t)
ysin = pH * np.sin(w*t)
A1 = 2 * ycos.sum() / N
B1 = 2 * ysin.sum() / N
C1 = math.sqrt(A1*A1+B1*B1)
print("y=%f+%fcos(%ft)+%fcos(%ft)"%(A0,A1,w,B1,w))
print("mean:%f"%A0)
print("amplitude:%f"%C1)
print("max pH:%f"%(A0+C1))
