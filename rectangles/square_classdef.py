from rectangle_classdef import *

class square (rectangle):
	def __init__(self, x=0, y=0, length=0.0):
		rectangle.__init__(self, x, y, length, length)\

	def setwidthandheight(self, length=0):

		if (length==0):
			print 
			print 'Sorry, you have not entered  valid length for this square'
			print

		self.width=length
		self.height=length

		print
		print'Operation completed successfully. Your square now has the following properties:'
		print
		print 'Legnth of Side = ', self.width
		print

	def show(self):
		print 'This square has the following properties:'
		print
		print 'Width: ', self.width
		print 'Height: ', self.height
		print 'X-Co-ordinate: ', self.x
		print 'Y-Co-ordinate: ', self.y