#run in fullscreen!

import sys,time
import random

content = open("pron20190403.txt").read()

#type function
def sprint(str):
		for c in str + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(1./200000)

#loading phase
#sprint(str(content))

while True:

	#listed phase (order)
	elements = content.split(" ")
	list.sort(elements)
	sprint(str(elements).replace(" ","     "))

	#windy phase (storm)
	elements = content.split(" ")
	sprint(str(elements).replace(" ",""))

	#random phase (chaos)
	random_element = random.choice(elements)
	random.shuffle(elements)
	sprint(str(elements).replace(" ",""))
