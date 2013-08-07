from basicshapeobject import *

class rectangle (basicshapeobject):
	def __init__(self, x=0, y=0, width=0.0, height=0.0):
		basicshapeobject.__init__(self, x, y)
		self.width=width
		self.height=height

	def show(self):
		print 'This rectangle has the following properties:'
		print
		print 'Width: ', self.width
		print 'Height: ', self.height
		print 'X-Co-ordinate: ', self.x
		print 'Y-Co-ordinate: ', self.y

	def setwidthandheight(self, width=0, height=0):

		if (width==0) or (height==0):
			print 
			print 'Sorry, you have not entered  valid width and height for this rectanagle'
			print

		self.width=width
		self.height=height

		print
		print'Operation completed successfully. Your rectangle now has the following properties:'
		print
		print 'Width = ', self.width
		print 'Height = ', self.height
		print

	def area(self):

		print 
		print'Area = ', (self.width * self.height)
		print
		return (self.width * self.height)

	def perimeter(self):
		
		print
		print 'Perimeter = ', ((2*self.width)+(2*self.height))
		print
		return ((2*self.width) + (2*self.height))

	def translate(self, xtrans=0, ytrans=0):
		self.x=self.x+xtrans
		self.y=self.y+ytrans

		print
		print 'Operation complete. Position Co-Ordinates are now as follows: x= ', self.x, ' y= ', self.y