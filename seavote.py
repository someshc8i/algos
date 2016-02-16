for tests in range(int(input())):
    lberror = 0
    uberror = 0
    value=0
    n=input()
    A=[int(i) for i in input().split()]
    for i in A:
        if i>0:
            lberror-=1
        value+=i
    diff=100-value
    if lberror<diff<=0:
        print("YES")
    else:
        print("NO") 