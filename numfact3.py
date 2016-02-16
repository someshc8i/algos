def num(x):
	d = 0
	while(x%2 == 0):
		d = d+1
		x = x /2
	if 2 in l:
		l[2] = l[2] + d
	else:
		l[2] = d
	i = 3
	while (x>1):
		if x%i == 0:
			if i in l:
				l[i] = l[i] +1 
			else:
				l[i] = 1
			x = x/i
		else:
			i = i + 2

import sys
n= int(input())
ansa = []
if n > 100:
	sys.exit(0)
for k in range(n):
	l = {}
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
			num(i)		
	else:
		sys.exit(0)
	ans = 1
	for i in l:
		ans = (l[i]+1)*ans
	ansa.append(ans)
for i in ansa:
	print(i)
		