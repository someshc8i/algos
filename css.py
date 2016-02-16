dict = {}
a = input()
a = a.split()
for i in range(len(a)):
	a[i] = int(a[i])
if a[0] in dict:
	if a[1] in dict[a[0]]:
		