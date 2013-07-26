from addressbook_class import *

class addressbookholder:
	'This class stores a collection of address books'
	
	def __init__(self):
		self.library={}

	def createbook(self, userspecbook):
		self.library[userspecbook.bookname]=userspecbook

	def viewallbooks(self):

		keybuffer=self.library.keys()
		keybuffer.sort()
		for eachKey in keybuffer:
			print eachKey

	def keysearcher(self, userspeckey):
		allkeys=self.library.keys()
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

	def viewonebook(self, userspecbookname):
		retreivedkey=self.keysearcher(userspecbookname)

		if retreivedkey=='bad':
			print
			print'Address Book not Found'
			print

		else:
			retreivedaddbook=self.library[retreivedkey]
			retreivedaddbook.briefallview()

	def deletebook(self, userspeckey):
		#retreivedkey=self.keysearcher(userspecbookname)

		# if retreivedkey=='bad':
		# 	print
		# 	print'Address Book not Found'
		# 	print

		# else:
		del self.library[userspeckey]
		print
		print 'Addressbook(', userspeckey, ') has been deleted successfully'
		print