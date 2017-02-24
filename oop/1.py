class man:
	def __init__(self,para,so):
		self.one = "twelve"
		self.para = para
		self.so = so
	def funky(self):
		print "Hey hey hey hey.."
	def printer(self):
		for us in self.para:
			print us,self.so
		

writer = man(['Yes','Guitar','HA!','Hie'],"Mr mr soul-sister")

writer.printer()

# class more:
# 	def __init__(self,*args):
# 		self.inli = args
# 		self.s = 0
# 	def sumise(self):
# 		for num in self.inli:
# 			self.s += num
# 		print self.s
		
# li = range(5)
# add = more(*li)
# add.sumise()

