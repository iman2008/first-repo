def fib (n):
	list=[]
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		b = (fib(n-1)+fib(n-2))
		list.append(b)
	print (list),
	return (b)
print (fib(10))
