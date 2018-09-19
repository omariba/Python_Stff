board = []
b = 0
e = 8
for i in range(8):
    if e <= 71:
		board.append(range(b,e))
		b = e
		e += 8

# if 4 in board[0:1][0]:
#     print board[0:1][0].index(4)

print board
