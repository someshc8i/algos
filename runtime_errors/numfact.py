n= int(input())
l = []
for k in range(n):
	a = input()
	a = a.split()
	for i in range(len(a)):
		a[i] = int(a[i])
	x=1
	for i in a:
		x=x*i
	print(x)
	a = 0
	for i in range(1,x+1):
		if x%i == 0:
			print(i)
			a = a+1
	l.append(a)
for i in l:
	print(i)
		