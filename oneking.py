t=int(input())
for _ in range(t):
    k=[]
    n=int(input())
    for i in range(n):
        l,r=map(int,input().split())
        k.append((r,l))
    #print(k)
    k=sorted(k)
    #print(k)
    count=0
    bomb=-1
    for x,y in k:
        if y>bomb:
            count=count+1
            bomb=x
    print(count)