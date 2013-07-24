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

		#print 'Address Card created for', self.actualcard[0].fieldvalue

	def display(self):
		print '----------------------------------------------------------------------------'
		print 'Displaying address card for:', self.actualcard[0].fieldvalue
		print ' '
		
		for item in self.actualcard:
			print item.fieldname, ':', item.fieldvalue

		print ' '
		print '----------------------------------------------------------------------------'

	def createnewfield(self, userspecname='NONE', userspecvalue='NONE'):
		fieldholder=addresscardobjects(userspecname, userspecvalue)
		self.actualcard.append(fieldholder)

		print ' '
		print self.actualcard[-1].fieldname, 'has been created with value:', self.actualcard[-1].fieldvalue
		print ' '

	def deletefield(self, userspecname):
		
		foundindex=self.fieldsearcher(userspecname)

		if foundindex[0]==True:

			del self.actualcard[foundindex[1]]
			print
			print 'Entry successfully removed'
			print ' '

		elif foundindex[1]==False:

			print 'Sorry. Entry not found'
			print ' '

	def editfield(self, userspecname, userspecvalue):

		foundindex=self.fieldsearcher(userspecname)

		if foundindex[0]==True:
			self.actualcard[foundindex[1]].fieldvalue=userspecvalue

			print self.actualcard[foundindex[1]].fieldname, 'has been changed. It is now:', self.actualcard[foundindex[1]].fieldvalue

		elif foundindex[0]==False:

			print 'Sorry. Entry not found'

	def renamefield(self, userspecoldname, userspecnewname):

		foundindex=self.fieldsearcher(userspecoldname)

		if foundindex[0]==True:
			self.actualcard[foundindex[1]].fieldname=userspecnewname

			print self.actualcard[foundindex[1]].fieldname, 'has been changed.'

		elif foundindex[0]==False:
			print 'Sorry. Entry not found'

	def fieldsearcher(self, userspecname):
		indexcounter=0

		for item in self.actualcard:
			searchtest=(item.fieldname.lower() == userspecname.lower())

			if searchtest==True:
				return [searchtest, indexcounter]
			else:
				indexcounter +=1