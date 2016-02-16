def partion(a , l , r , k):
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
		if k == i-1:
			return a[i-1]
		elif k<i-1:
			select(a[0:i-2] , i-1 , k)
		else:
			select(a[i:r] , r-i+2 , i-1-k)

def select(a , l , k):
	if l == 1:
		return a[i]
	partion (a , 0 , l-1 , k)

a = [1,3,5,2,3,4,6,3,1 ,8,5,2,4,5,7,7,2,2,4,6,9,8]
x = select(a , len(a) , 5)
print(x)

