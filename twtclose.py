t = {}
n = input()
n = n.split()
for i in range(int(n[0])):
	t[i+1] = 1
	
def revert(a):
	if t[a] == 0 :
		t[a] = 1
	else:
		t[a] = 0
		
ansa = []
for func in range(int(n[1])):
	f = input()
	f = f.split()
	if f[0] == 'CLOSEALL':
		for i in t:
			t[i] = 1
	else:
		revert(int(f[1]))
	ans = 0
	for i in t:
		if t[i] == 0:
			ans = ans +1
	ansa.append(ans)

for i in ansa:
	print(i)
