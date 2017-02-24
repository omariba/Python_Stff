u = input("Num:")

#board creation
b = []
s = 0
d = 8
for i in range(8):
	b.append(range(s,d))
	s = d
	d += 8

#getting numbers position
for p in b:
	if u in p:
		y = b.index(p)
		x = p.index(u)

u1,u2,d1,d2,l1,l2,r1,r2 = y-1,y-2,y+1,y+2,x-1,x-2,x+1,x+2

if y == 0:
	if x in range(2,6):
		print b[d1][l2]
		print b[d1][r2]
		print b[d2][l1]
		print b[d2][r1]
	elif x == 1:
		print b[d1][r2]
		print b[d2][r1]
		print b[d2][l1]
	elif x == 0:
		print b[d1][r2]
		print b[d2][r1]
	# elif x == 6:
		
# def landingSpot():
# 	allm = [18, 19, 20, 21, 26, 27, 28, 29, 34, 35, 36, 37, 42, 43, 44, 45]
# 	tr = [0,1,8,9]
# 	tm = [2,3,4,]

# 	if u in allm:
# 		print b[u1][l2]
# 		print b[u1][r2]
# 		print b[u2][l1]
# 		print b[u2][r1]
# 		print b[d1][l2]
# 		print b[d1][r2]
# 		print b[d2][l1]
# 		print b[d2][r1]
# 	elif u in tr:
# 		print b[d1][r2]
# 		print b[d2][r1]
# 		print b[u1][r2]

# landingSpot()