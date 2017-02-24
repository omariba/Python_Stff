class robberslang:
	def __init__(self):
		self.vowels = ['a','e','i','o','u',' ']
		self.sentence = raw_input("Enter words to translate:\n")
		self.trans = []
	def translate(self):
		for l in self.sentence:
			if l not in self.vowels:
				pla = l+'o'+l
				self.trans.append(pla)
			else:
				self.trans.append(l)
		print ''.join(self.trans)

clacc = robberslang()
clacc.translate()