class setwe:
	def __init__(self,name):
		self.name = name
	def speak(self):
		print "Finally I can breath " + self.name

man = setwe("Mandela")
man.speak()