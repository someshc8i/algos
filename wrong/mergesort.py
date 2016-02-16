def mergesort(a, p, r):
  if p<r:
    if r%2 == 0:
      q=int((p+r)/2)
      mergesort(a , p , q)
      mergesort(a , q+1 , r)
      merge(a , p , q , r)

      
    else:
      q=int((p+r-1)/2)
      mergesort(a , p , q)
      mergesort(a , q+1 , r)
      merge(a , p , q , r)

def merge(a,p,q,r):
  m = q-p+1
  print("m is %s" %(m))
  n= r-p
  print("n is %s" %(n))
  print("q is %s" %(q))
  x=[]
  y=[]
  for i in range(0 , m):
    print(i)
    x.append(a[p+i])
  print (x)
  for j in range(0 , n):
    y.append(a[q+j+1])
  print(y)
  x.append(99)
  y.append(99)
  print (x)
  print (y)
  i=0
  j=0
  for k in range(p , r+1):
    print(k)
    if (x[i] <= y[j]):
      a[k] = x[i]
      i = i+1
    else:
      a[k] = y[j]
      j = j+1
  print(a)
a = [5, 1 ,5 , 3]
mergesort(a , 0, len(a)-1)
print(a)
