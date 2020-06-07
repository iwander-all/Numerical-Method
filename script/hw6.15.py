import math
import numpy as np
import matplotlib.pyplot as plt


# fixed-point iteration

xi = 1.2
yi = 1.2

for i in range(10):
	xiplus = math.sqrt(xi+0.75-yi)
	yiplus = (xi*xi - yi) / (5 * xi)
	xi = xiplus
	yi = yiplus
	print("x:",xi)
	print("y:",yi)


#Newton- Raphson method

xi = 1.2
yi = 1.2

for i in range(10):
	ui = -xi*xi + xi + 0.75 - yi
	vi = xi*xi - yi - 5 * xi * yi
	dvi_y = -1 - 5 * xi
	dvi_x = 2 * xi - 5 * yi
	dui_y = -1
	dui_x = -2 * xi + 1
	xiplus = xi - (ui*dvi_y - vi*dui_y) / (dui_x*dvi_y - dui_y*dvi_x)
	yiplus = yi - (vi*dui_x - ui*dvi_x) / (dui_x*dvi_y - dui_y*dvi_x)
	xi = xiplus
	yi = yiplus
	print("x:",xi)
	print("y:",yi)
