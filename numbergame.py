testcases = int(input())
ans = list()

for x in range(testcases):
  n = int(intput())
  for y in range(1, n):
    if n % (n-y) == 0:
	  n = y
  