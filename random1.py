#defining 10 random number between 10 and 20

import random

def random_numer():
	i=0
	while (i<=10):
		x = random.random() * 20
		if 10 <= x <= 20:
			print (x)
			i=i+1
random_numer()

