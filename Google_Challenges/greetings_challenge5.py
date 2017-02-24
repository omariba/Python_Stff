def answer(s):
	g = 0
	for n,i in enumerate(s):
		if i == "<":
			for f in s[:n]:
				if f == ">":
					g += 2
				
	print g
answer("<<>><")
