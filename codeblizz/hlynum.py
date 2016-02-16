n = input()
n = n.split()
for i in range(len(n)):
	n[i] = int(n[i])
isl = input()
isl = isl.split()
for i in range(len(isl)):
	isl[i] = int(isl[i])
for _ in range(n[1]):
	temp = []
	ans= []
	q = input()
	q = q.split()
	for i in range(len(q)):
		q[i] = int(q[i])
	for i in range(q[0]-1 , q[1]):
		temp.append(isl[i])
	temp = sorted(temp)
	i= 1
	while temp[0]>1 and i <= temp[0]:
		k = 0
		for j in temp:
			if j%i !=0:
				k = k+1
		if k ==0:
			temp[0] = temp[0]/i
			ans.append(i)
		i = i+1
	print(ans)
	f = 1
	for i in ans:
		f = f*i
	print(f)
			
		