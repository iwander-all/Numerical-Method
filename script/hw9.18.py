import numpy as np

a = np.array([[0,0,0,0],[0,1,2,-1],[0,5,2,2],[0,-3,5,-1]],dtype = np.float64)
b = np.array([[0],[2],[9],[1]],dtype = np.float64)
n = 3
tol = 0.0001
er = 0
s = np.array([],dtype = np.float64)
x = np.array([],dtype = np.float64)
for i in range(n+1):
	list = [1]
	temp1 = np.array(list,dtype=np.float64)
	s = np.append(s,temp1)
	x = np.append(x,temp1)
print(s,x)

def gauss():
	global a,b,n,x,tol,er,s
	er = 0
	for i in range(1,n+1):
		s[i] = abs(a[i][1])
		for j in range(2,n+1):
			if (abs(a[i][j])>s[i]):
				s[i] = abs(a[i][j])
	eliminate()
	if (er != -1):
		substitute()
		
def eliminate():
	global a,b,n,x,tol,er,s
	for k in range(1,n):
		#pivot(k)
		if (abs(a[k][k]/s[k])<tol):
			er = -1
			break
		for i in range(k+1,n+1):
			print('a[i][k]',a[i][k])
			print('a[k][k]',a[k][k])
			factor = a[i][k]/a[k][k]
			for j in range(k+1,n+1):
				a[i][j] = a[i][j] - factor*a[k][j]
			b[i] = b[i] - factor*b[k]
	if(abs(a[k][k]/s[k])<tol):
		er = -1
		
def pivot(k):
	global a,b,n,x,tol,er,s
	p = k
	big = abs(a[k][k]/s[k])
	for ii in range(k+1,n+1):
		dummy = abs(a[ii][k]/s[ii])
		if (dummy > big):
			big = dummy
			p = ii
	if (p!=k):
		for jj in range(k,n):
			dummy = a[p][jj]
			a[p][jj] = a[k][jj]
			a[k][jj] = dummy
		dummy = b[p]
		b[p] = b[k]
		b[k] = dummy
		dummy = s[p]
		s[p] = s[k]
		s[k] = dummy
			
def substitute():
	global a,b,n,x,tol,er,s
	x[n] = b[n]/a[n][n]
	for i in range(n-1,0,-1):
		sum = 0
		for j in range(i+1,n+1):
			sum = sum + a[i][j]*x[j]
		x[i] = (b[i]-sum)/a[i][i]
	
gauss()	
	
print(x)	
	
	







