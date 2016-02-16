n = int(input())
for k in range (n):
	a = input()
	a = a.split()
	for i in range(len(a)):
		a[i] = int(a[i])
	b = input()
	b= b.split()
	for i in range(a[0]):
		b[i] = int(b[i])
	f = 0
	for i in range(a[0]):
		if ((b[i]+a[1])%7 == 0):
			f = f + 1
	print(f)