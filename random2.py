#creats a list with the length of w and put w random items on that

import random

w = int(input("please enter how many numbers you need"))
r = [0]*w
for i in range (w):
	r[i]=random.random()
print (r)

