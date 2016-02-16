n = int(input())
a=[]
for i in range(n):
	a.append([])
	f = int(input())
	for j in range(n):
		a[i].append(f%10)
		f = f//10
for i in range(n):
	a[i].reverse()
req = 0
for i in range(n):
	for j in range(n):
		if a[i][j]==0:
			if i != j:
				for x in range(n):
					req = req + a[i][x]*a[x][j]
						
print(req)