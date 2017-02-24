def answer(data, n):
	g = []
	for i in data:
		if data.count(i) <= n:
			g.append(i)
	print g


answer([12,1,3,4,5,5,7],1)