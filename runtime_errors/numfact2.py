def num(x):
	d=1
	while(x%2 == 0):
		d = d+1
		x = x /2
	a = 1
	i = 3
	j = 0
	l = [1]
	while (x>1):
		if x%i == 0:
			a = a+1
			l[j] = a
			x = x/i
		else:
			l.append(1)
			j = j +1
			i = i + 2
			a=1
	for i in l:
		d = d*i
	return(d)



import sys
n= int(input())
l = []
if n > 100:
	sys.exit(0)
for k in range(n):
	o = int(input())
	if o > 10:
		sys.exit(0)
	a = input()
	a = a.split()
	if len(a) == o:
		for i in range(len(a)):
			a[i] = int(a[i])
		x=1
		for i in a:
			x=x*i
		l.append(num(x))
	else:
		sys.exit(0)
for i in l:
	print(i)
		