import sys
n = int(input())
if n <= 40:
	a = ["A" ,"D" , "O" , "P" , "Q" , "R"]
	b = ["B"]
	f = []
	for i in range (n):
		c = input()
		x = 0
		for j in c:
			if j in a:
				x = x+1
			elif j in b:
				x = x+2
		f.append(x)
	
	for i in f:
		print(i)
else:
	sys.exit(0)