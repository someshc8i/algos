x = input()
x = x.split()
for i in range(len(x)):
	x[i] = int(x[i])
n = x[0]
q = x[1]
c =[]
for i in range(n):
	c.append(1)
l=[]

def flip(a,b):
	for i in range(a,b+1):
		if c[i] == 0:
			c[i] = 1
		else:
			c[i] = 0
def count(a ,b):
	d = 0
	for i in range(a , b+1):
		if c[i] == 0:
			d=d+1
	l.append(d)
	
for i in range(q):
	a = input()
	a = a.split()
	for i in range(len(a)):
		a[i] = int(a[i])
	if a[0] == 0:
		flip(a[1] , a[2])
	else:
		count(a[1], a[2])
		
for i in l:
	print(i)

