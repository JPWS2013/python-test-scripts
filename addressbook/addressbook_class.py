from addresscard_class import *

class addressbook:
	'This class creates an object which is essentially a collection of adddress cards'

	def __init__(self, userspecbookname='NONE'):

		self.bookname=userspecbookname
		self.actualdictionary={}

	def addcard(self, userspeccard):

		self.actualdictionary[userspeccard.actualcard[0].fieldvalue]=userspeccard

	def viewcard(self, userspeccardname):
		keyretreived=self.keysearcher(userspeccardname)
		#testforkey=self.actualdictionary.has_key(userspeccardname)

		if keyretreived=='bad':
			print ' '
			print 'Specified address card not found'
			print ' '

		else:
			card=self.actualdictionary[keyretreived]
			card.display()

	def retrievecard(self, userspeccardname):
		#print userspeccardname
		#testforkey=self.actualdictionary.has_key(userspeccardname)
		keyretreived=self.keysearcher(userspeccardname)
		#print testforkey

		if keyretreived=='bad':
			#print 'Specified address card not found'
			return 'bad'

		else:
			card=self.actualdictionary[keyretreived]
			return card

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

		deletecheck=self.actualdictionary.haskey(userspeccardname)

		if deletecheck==True:
			del self.actualdictionary[userspeccardname]

		elif deletecheck==False:
			print
			print 'Sorry. Contact not found'
			print

	def keysearcher(self, userspeckey):
		allkeys=self.actualdictionary.keys()
		indexcounter=0
		foundkey='bad'

		for eachkey in allkeys:
			test=(eachkey.lower()==userspeckey.lower())
			if test ==True:
				foundkey=eachkey
				break
			else:
				indexcounter += 1
		if foundkey=='bad':

			return 'bad'

		else:
			return allkeys[indexcounter]

	def briefallview(self):
		contactlist=self.actualdictionary.keys()
		contactlist.sort()

		print '-----------------------------------------------------------------------------'
		print 'Displaying contacts in current address book (Brief View):'
		print
		for eachkey in contactlist:
			print eachkey
		print 
		print '-----------------------------------------------------------------------------'

	def fullallview(self):
		print '-----------------------------------------------------------------------------'
		contactlist=self.actualdictionary.keys()

		if len(contactlist)==0:
			print
			print 'NO CONTACTS CONTAINED IN THIS ADDRESS BOOK'
			print

		else:
			contactlist.sort()		
			print 'Displaying contacts in current address book (Full View):'
			print
			for eachkey in contactlist:
				tempholder=self.actualdictionary[eachkey]
				tempholder.display()
			print 
		print '-----------------------------------------------------------------------------'

	