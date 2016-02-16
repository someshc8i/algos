n = int(input())
for test in range(n):
	a = input()
	b = input()
	ans = 0
	for i in b:
		if i in a:
			ans = ans +1
	print(ans)