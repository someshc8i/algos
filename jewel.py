t=int(input())
for x in range(t):
    perl=input()
    s=perl.split()
    count=0
    prev=[]
    for c in s[0]:
        temp=s[0].count(c)
        if c not in prev:
            prev.append(c)
            count+=int(temp/2)
            if temp%2==1:
                count+=1
    print(int(count)) 