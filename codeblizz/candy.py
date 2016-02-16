n =  int(input())
c = input()
c= c.split()
for i in range(len(c)):
	c[i] = int(c[i])
max = c[0]
for i in range(n-1):
	if c[i+1] > max:
		max = c[i+1]
print(max)