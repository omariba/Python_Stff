data = [1,1,2,3]

n = 2

li = []

#def answer(data,n):
#	for i in data:
#		if data.count(i) == n:
#			li.append(i)
#	print li

def answer(data,n):
	for i in data:
		if data.count(i) != n:
			data.remove(i)
	print data
	
answer(data,n)
