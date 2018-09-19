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
def column_pos(num):
	c1 = 0
	c2 = 1
	while num not in board[c1:c2][0]:
    		c1+=1
		c2+=1
	else:
    		# print "c =",c1, "r =",board[c1:c2][0].index(num)
			return c1

def column_dif(beg,fin):
    	c_a = column_pos(beg)
	c_b = column_pos(fin)
    	return abs(c_a-c_b)

def move_count(start,stop):
    	one = [6,19,15,17]
    	if column_dif(start,stop) == 1 and abs(start-stop) == 6:
    			return 1
	if column_dif(start,stop) == 1 and abs(start-stop) == 10:
    			return 1
	if column_dif(start,stop) == 2 and abs(start-stop) == 17:
    			return 1
	if column_dif(start,stop) == 2 and abs(start-stop) == 15:
    			return 1
	if abs(start-stop) not in one:
    		if start < 48:
				
    		return 0

print move_count(0,1)
print board

#To do
# - Find all possible next positions x-wards(column) +2,-2,+1,-1
# - Find all possible next positions y wards(row) +6,-6,+10,-10,+17,-17,+15,-15
# - Do this with all new positions until you arrive at destination
