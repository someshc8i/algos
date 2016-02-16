def compare(d , a , b):                  #wrong alogorithm
	n = len(d)
	if d[a] < d[b]:
		if a == (n/2)+1:
			d[a] = d[b]
			for i in range(a):
				d[n-1-i] = d[i]
		else:
			d[int((n/2)+1)] = d[int((n/2)+1)]+1
			d[int(n/2-1)] = d[int(n/2-1)] +1
			for i in range(int((n/2)-1)):
				d[n-1-i] = d[i]
	elif d[a] > d[b]:
		for i in range(a+1):
			d[n-1-i] = d[i]
	else:
		compare(d , a-1 , b+1)
	print(d)

n = int(input())
i=0
d = []
x = n
while x > 1:
	d.append(int(x%10))
	x = x/10
	i = i+1
print(i)
print(d)
for i in range(int(len(d)/2)):
	k = d[i]
	d[i] = int(d[len(d)-1-i]) 
	d[len(d)-1-i] = int(k)
print(d)
compare(d , int((len(d)/2)-1) , int(len(d)/2))

