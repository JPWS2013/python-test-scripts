class basicshapeobject:
	def __init__(self, x=0, y=0):
		self.x=x
		self.y=y

	def setposition(self, x, y):

		self.x=x
		self.y=y

		print
		print 'Operation completed successfully. Your shape is now positioned at: x= ', self.x, ' and y= ', self.y
		print
