A={}
def coins(n):
    if n <=11:
        return (n)
    elif n in A:
        return A[n]
    else:
        s=max(n,(coins(n//2)+coins(n//3)+coins(n//4)))
        A[n]=s
        return s

for k in range(10):
	n = int(input())
	print(coins(n))

	
	
