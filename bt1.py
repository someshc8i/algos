bt = [8 , -1 ,-1]
def insert(a ,n):
	if n<=a[0]:
		if a[1] == -1:
			a[1] = [n , -1 ,-1]
		else:
			insert(a[1], n)
	else:
		if a[2] == -1:
			a[2] = [n , -1 ,-1]
		else:
			insert(a[2] , n)

insert(bt , 5)
insert(bt , 9)
insert(bt , 4)
insert(bt , 6)

print(bt)

""" pointers from parent to child but not from child to parent"""