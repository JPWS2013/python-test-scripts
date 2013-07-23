from addresscard_class import *

class addressbook:
	'This class creates an object which is essentially a collection of adddress cards'

	def __init__(self, userspecbookname='NONE'):

		self.actualdictionary={}

	def addcard(self, userspeccard):

		self.actualdictionary[userspeccard.actualcard[0].fieldvalue]=userspeccard

	def viewcard(self, userspeccardname):
		
		testforkey=self.actualdictionary.has_key(userspeccardname)

		if testforkey==True:
			card=self.actualdictionary[userspeccardname]
			card.display()

		elif testforkey==False:
			print ' '
			print 'Specified address card not found'
			print ' '

	def retrievecard(self, userspeccardname):
		#print userspeccardname
		testforkey=self.actualdictionary.has_key(userspeccardname)
		#print testforkey

		if testforkey==True:
			card=self.actualdictionary[userspeccardname]
			return card

		elif testforkey==False:
			print 'Specified address card not found'
			return 'bad'

	def dictionarycleanup(self):
		bookentries=self.actualdictionary.keys()
		for item in bookentries:
			cleantest=(item.lower()==self.actualdictionary[item].actualcard[0].fieldname.lower())

			if cleantest==True:
				continue
			elif cleantest==False:
				cardbuffer=retrievecard(item)
				self.addcard(cardbuffer)
				del self.actualdictionary[item]

	def removecard(self, userspeccardname):
		del self.actualdictionary[userspeccardname]