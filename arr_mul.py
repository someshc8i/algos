def arr_mul(a , b , c):
  for i in range(0 , c):
    for j in range(0 , c):
      x=0
      for k in range(0 , c):
        x = x + a[k][j]*b[i][k]
      m[i].append(x)

m = [[],[]]  
a = [[1,2] , [2,3]]
b = [[2,3] , [3,4]]
arr_mul(a ,b ,len(m))
print(m)