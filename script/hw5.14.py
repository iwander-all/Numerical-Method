import math

xl = 3.
xu = 5.
e = 1.
xr_old = xu
i = 1

while(e > 0.02):
	print('\n')
	print("----------Round",i,"----------")
	i+=1
	xr_new = (xl + xu) / 2
	e = abs((xr_new-xr_old) / xr_new)
	xr_old = xr_new
	yr = 9.81*80/xr_new *(1-math.exp(-xr_new/20))-36
	yl = 9.81*80/xl *(1-math.exp(-xl/20))-36
	yu = 9.81*80/xu *(1-math.exp(-xu/20))-36
	print("xl:",xl)
	print("yl:",yl)
	print("xu:",xu)
	print("yu:",yu)
	print("xr:",xr_new)
	print("yr:",yr)
	print("e:",e)
	if(yl*yr<0):
		xu = xr_new
		continue
	if(yl*yr>0):
		xl = xr_new
		continue
	if(yl*yr==0):
		print("result:", xr_new)
		break
