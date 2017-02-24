class reverseall:
	def __init__(self):
		self.word = raw_input("Enter A Word:")
	def revword(self):
		print self.word[::-1]

clacc = reverseall()
clacc.revword()