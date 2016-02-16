def palin(d , c , x):
	hld = len(d)//2
	if c != hld:
		if d[hld + c] > d[hld -x-c]:
			if c ==0:
				d[hld-x] = d[hld-x] +1
				show(d,x)
			else:
				d[hld] = d[hld-x] = d[hld]+1
				show(d,x)
		elif d[hld +c] < d[hld -x - c]:
			show(d,x)
		else:
			c = c+1
			palin(d , c , x)
	else:
		d[hld] = d[hld-x] = d[hld]+1
		show(d,x)

def show(d, x):
	hld = len(d)//2
	for i in range(hld):
		d[2*hld - x -i] = d[i]
	x = ''
	for i in d:
		x = x+str(i)
	print(int(x))
test = int(input())
for _ in range(test):
	n = int(input())
	a = []
	while n > 1:
		a.append(int(n%10))
		n = n/10
	a.reverse()
	if len(a)%2==0:
		palin(a, 0 , 1)
	else:
		palin(a, 0 , 0)