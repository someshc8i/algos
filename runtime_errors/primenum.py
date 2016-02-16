n = int(input())
if n > 10:
	sys.exit(0)
for test in range(n):
	num = input()
	num  = num.split()
	num[0] = int(num[0])
	num[1] = int(num[1])
	p = []
	ansa = []
	for i in range(2,num[1]+1):
		k = 0
		for j in p:
			if i%j == 0:
				k = 1
				break
		if k == 0:
			if i >= num[0]:
				ansa.append(i)
			p.append(i)
	for i in ansa:
		print(i)