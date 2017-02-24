board = []
s = 0
d = 8
for i in range(8):
	board.append(range(s,d))
	s = d
	d += 8
