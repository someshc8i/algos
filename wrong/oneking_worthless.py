k = int(input())
v = {}
for king in range(k):
	a = input()
	a=a.split()
	a[0] = int(a[0])
	a[1] = int(a[1])
	for i in range(a[0] , a[1]+1):
		if i in v:
			v[i].append(king)
		else:
			v[i] = [king]
			
def find_max(a):
	max = 0
	num = []
	k = 0
	for i in a:
		if len(a[i])>max:
			max = len(v[i])
			numi = i
			k = 1
		else:
			continue
	if k == 1:
		for i in a:
			if len(a[i]) == len(a[numi]):
				num.append(i)
	return(num)
	
def redefine_v(a , k):
	temp=[]
	for i in a[k]:
		temp.append(i)
	for i in temp:
		for j in a:
			v=0
			while v < len(a[j]):
				if a[j][v] == i:
					a[j].pop(v)
				else:
					v=v+1
"""				
def max_bombs( c, a):
	for x in range(len(find_max(a))):
		print(x)
		print(find_max(a))
		if len(find_max(a))>0:
			c = c +1
			redefine_v(a , find_max(a)[x])
			max_bombs(c ,a)
		else:
			print(c)
			ans.append(c)"""
	
def max_bombs(c,a):
	print(k)
	x = find_max(a)
	print(x)
	if len(x)==0:
		print(c)
		ans.append(c)
	else:
		c = c + 1
		for i in range(len(x)):
			print(i)
			redefine_v(a , x[i])
			max_bombs(c , a)
	
print(v)
ans =[]
max_bombs(0 ,v )
for i in ans:
	print(i)

print(v)