import numpy as np

v = np.zeros(20) 
v[0] = -20.
c = 10.
m = 80.
print(v[0])

for i in range(19):
	if i == 9:
		c = 50
	v[i+1] = v[i] + (9.8 - c/m * v[i])
	print(v[i+1])
