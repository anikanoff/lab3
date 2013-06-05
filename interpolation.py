

def parabolinter(x,y):  # returning koeff a,b,c
	n=len(x)
	koeff=[0,0,0]
	delta =[0,0,0,0]
	a=[[0]*3 for i in range(3)]
	b=[0,0,0]
	a[0][0]=1
	a[1][0]=1
	a[2][0]=1
	a[0][1]=x[0]
	a[1][1]=x[int(n/2)-1]
	a[2][1]=x[-1]
	a[0][2]=a[0][1]*a[0][1]
	a[1][2]=a[1][1]*a[1][1]
	a[2][2]=a[2][1]*a[2][1]
	b[0]=y[0]
	b[1]=y[int(n/2)-1]
	b[2]=y[-1]
	delta[0]=operator(a)
	i=0
	j=0
	while j<3:
		a1=newarr(a)
		while i<3:
			a1[i][j] = b[i]
			i=i+1
		delta[j+1]=operator(a1)
		j=j+1
		i=0
		a1=a
	while i<3:
		koeff[i] = delta[i+1]/delta[0]
		i=i+1
	print('y(x) ='+"%.4f"%(float(koeff[0]))+'+'+"%.4f"%(float(koeff[1]))+'x+'+"%.4f"%(float(koeff[2]))+'x^2')
	return koeff
def operator(a): # counting operator of matrix[3][3] dlya reweniya systemi metodom Kramera
	s = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[1][0]*a[2][1]*a[0][2] - a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[2][1]*a[1][2]
	return s
def newarr(a): #making identical matrix
	i=0
	a1=[[0]*3 for i in range(3)]
	while i<3:
		j=0
		while j<3:
			a1[i][j]=a[i][j]
			j=j+1
		i=i+1
	return a1


