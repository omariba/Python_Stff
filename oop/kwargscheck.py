class kwargscheck:
	def __init__(self,**kwargs):
		self.args = kwargs
	def print_args(self):
		for key,value in self.args.iteritems():
			print key
			print value

li = {'nel':1,'man':2,'nelk':3}
clac = kwargscheck(**li)
clac.print_args()