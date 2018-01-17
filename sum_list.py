my_list = [1,3,45,43,23,[23,423,[23,42],43],43,[5,67,56]]
def listadder(mlist):
	total_sum=0
	l_list=mlist 
	for item in l_list:
		if isinstance(item,int):
			total_sum = total_sum + item 
		elif isinstance(item,list):
			total_sum = total_sum + listadder(item)
		else:
			print("list contains things other than lists and numbers")
			break
	return (total_sum)
print (listadder([1,2,3,[1,[2,3]]]))
