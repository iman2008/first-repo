import math
def square ():
	side=int(input("please enter side here: "))
	return side*side

def circle ():
	radius=int(input("please enter radius here"))
	return math.pi*((radius**2))
def sphere ():
	radius=int(input("please enter radius here: "))
	return math.pi*2*radius

print("if you need square please type 1 \n if you need circle please type 2 \n	if you need sphere please type 3")

x = int(input("please enter what you need"))
if x==1:
	print(square())
if x==2:
	print(circle())
if x==3:
	print (sphere())
