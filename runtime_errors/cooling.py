t = int(input())
if t<=30:
	l = []
	for x in range(t):
		n = int(input())
		if n <= 30:
			a = input()
			a = a.split()
			b = input()
			b = b.split()
			for i in range(n):
				a[i] = int(a[i])
				b[i] = int(b[i])

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

			partition(a , 0 , len(a))
			partition(b , 0 , len(b))
			i = 0
			j = 0
			f = 0
			for k in range(n):
				if (a[i] <= b[j]):
					i = i+1
					j = j+1
					f = f+1
				else:
					j = j+1
			l.append(f)
	for i in l:
		print(i)
		
		
"""can be implemented with heaps and extract min every time"""