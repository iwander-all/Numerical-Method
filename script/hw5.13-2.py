import numpy as np
import math

xl = 40.
xu = 60.
e = 1.
x_old = 40.

while (e > 0.001):
	yl = 9.8 / 15 * xl *(1 - math.exp(-135 / xl)) - 35	
	yu = 9.8 / 15 * xu *(1 - math.exp(-135 / xu)) - 35
	xr = xu - yu * (xl - xu) / (yl - yu)
	yr =  9.8 / 15 * xr *(1 - math.exp(-135 / xr)) - 35
	e = abs((xr - x_old) / xr)
	x_old = xr
	print("xr:",xr)
	print("e:",e)
	if (yr * yu < 0):
		xl = xr
	if (yr * yu > 0):
		xu = xr	
	if (yr * yu == 0):
		break










