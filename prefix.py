def count(b):
	x = 0
	for i in range(len(a)):
		if a[i] == b[i]:
			x = x+1
		else:
			break
	return(x)
n = int(input())
a = input()
b = input()
b = 2*b
lenb= len(b)//2
shift = 0
max = 0
for i in range(lenb):
	if count(b[i:lenb+i])>max:
		max = count(b[i:lenb+i])
		shift = i
print(shift)
		