def partition(a , l , r):
	if l < r:
		p = a[l]
		i = l+1
		for j in range(l+1 , r):
			if a[j] < p:
				k = a[j]
				a[j] = a[i]
				a[i] = k
				i = i+1
		k = a[l]
		a[l] = a[i-1]
		a[i - 1] = k
		partition(a ,0 , i-2)
		partition(a ,i ,r)

a = [1,3,5,3,4,6,3,1 ,8,5,2,4,5,7,7,7,7,2,2,4,6,9,8]
partition(a , 0 , len(a))
print(a)
l =0
maxn = a[0]
repn = 1
for i in range(1 , len(a)):
	if a[i] == a[i-1]:
		l = l+1
	elif l > repn:
		repn = l
		l = 1
		maxn = a[i-1]
	else:
		l = 1
print(maxn)
print(repn)

