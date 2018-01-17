
def sum_adder (mlist):
	"""this will add up the content of the list"""
	total = 0
	s_list = mlist
	for item in s_list:
		if isinstance(item,int):
			total = total + item
		elif isinstance (item,list):
			total=total+sum_adder (item)
		else:
			return "you have not select proper list"
	return total
x = [90,10,11]
print (sum_adder(x))
