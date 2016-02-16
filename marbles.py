for t in range(int(input())):
    n, k = map(int, input().split())
    result = 1
    
    n-=1
    k-=1
    
    if k==0 or n==k:
        result = 1
    elif k==1 or n==k-1:
        result = n
    else:
        if k > n//2:
            k = n-k
        for i in range(k):
            result *= (n-i)
            result //= (i+1)
    print(result)