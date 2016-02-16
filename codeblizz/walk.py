def rec( x , y):
	if y == x:
		print("YES")
	if y < x :
		rec(x , y +2*y)
		rec(x , y +3*y)

test = int(input())
for _ in range(test):
	ans = 0
	n = input()
	n = n.split()
	for i in range(len(n)):
		n[i] = int(n[i])
	rec( n[0] ,n[1])
	if ans == 0:
		print("NO")
	else:
		print("YES")
		
