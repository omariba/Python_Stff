#li = [1,2,3,4,5]

#def summ(args):
#    length = len(args)
#    lim = 0
#    tot = 0
#    while lim < length:
#        tot += args[lim]
#        lim += 1
#	print tot

#summ(li)

#me = []
#def nel(*args):
#	while True:
#		m = input("Enter numbers To a list(enter non digits to exit)")
#		if type(m) == str:
#			break
#		else:
#			me.append(m)
#			lengt = len(args)
#	print lengt 
		
#nel(1,*me)
import time
import os

def funny(*args):
	s = 0
	m = 1
	for k in args:
		s += k
		m *= k
	print "Your total sum is %s" % s
	print "Your product is %s" % m

li = []

while True:
	v = input("Enter numbers To a list(enter 00 to exit): ")
	if v != 00:
		li.append(v)
	else:
		os.system('clear')
		print "Calculating"
		time.sleep(1)
		os.system('clear')
		print "Calculating."
		time.sleep(1)
		os.system('clear')
		print "Calculating.."
		time.sleep(1)
		os.system('clear')
		print "Calculating..."
		time.sleep(0.5)
		funny(*li)
		break

	
