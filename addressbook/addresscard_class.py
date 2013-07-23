from addresscardobjects import *

class addresscard:
	'This class creates an object which stores personal information in an address card which may be retrieved later. Its partner class is the addressbook class'

	def __init__(self, userspecname='NONE', userspeccp='NONE'):
		'Creates a new address card with at least name and cell phone number instance variables'

		self.actualcard=[]

		fieldholder=addresscardobjects('Name', userspecname)
		self.actualcard.append(fieldholder)

		fieldholder=addresscardobjects('Mobile Phone Number', userspeccp)
		self.actualcard.append(fieldholder)

		print 'Address Card created for', self.actualcard[0].fieldvalue

	def display(self):
		print 'Displaying address card for:', self.actualcard[0].fieldvalue
		print ' '
		
		for item in self.actualcard:
			print item.fieldname, ':', item.fieldvalue

		print ' '

	def createnewfield(self, userspecname='NONE', userspecvalue='NONE'):
		fieldholder=addresscardobjects(userspecname, userspecvalue)
		self.actualcard.append(fieldholder)

		print self.actualcard[-1].fieldname, 'has been created with value:', self.actualcard[-1].fieldvalue