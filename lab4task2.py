from functools import reduce

a = []
for i in range (100,500):
	if (i%2==0):
		a.append(i)
def sum (x,y):
	w=x+y
	return w

x = reduce (sum,a)
print (x) 
