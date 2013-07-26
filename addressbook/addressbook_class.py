from addresscard_class import * #Imports all address card class definitions 

class addressbook:
	'This class creates an object which is essentially a collection of adddress cards' #Describes the purpose of the addressbook class

	def __init__(self, userspecbookname='NONE'): #Defines how an address book should be created

		self.bookname=userspecbookname #Creates an address book name, whether the user specifies one or not (Necessary for retrieval from the address book library)
		self.actualdictionary={} #Creates a dictionary object to store the address cards 

	def addcard(self, userspeccard): #Instance method to add cards to the address book

		self.actualdictionary[userspeccard.actualcard[0].fieldvalue]=userspeccard #Adds the card to the address book dictionary object

	def viewcard(self, userspeccardname): #Instance method to display the address card
		keyretreived=self.keysearcher(userspeccardname) #Uses the keysearcher method defined within the addressbook to search for the address card specified by the user
		#testforkey=self.actualdictionary.has_key(userspeccardname)

		if keyretreived=='bad': #Keysearcher returns "bad" if key not found; So here checking if an address card was found
			print ' '
			print 'Specified address card not found' #If no card found, indicate so to the user
			print ' '

		else: #Else if a card is found
			card=self.actualdictionary[keyretreived] #Retrieve it into a buffer variable
			card.display() #Use the display instance method defined for addresscard objects to display the card

	def retrievecard(self, userspeccardname): #Instance method to retreive a card from address book
		#print userspeccardname
		#testforkey=self.actualdictionary.has_key(userspeccardname)
		keyretreived=self.keysearcher(userspeccardname) #Employs the keysearcher instance method to search for the specified contact
		#print testforkey

		if keyretreived=='bad': #If contact not found
			#print 'Specified address card not found'
			return 'bad' #Return "bad" as an indicator to the programme that no contact found

		else: #If contact found
			card=self.actualdictionary[keyretreived] #Retrieve the card into a buffer
			return card #Return the card to the programme for action

	def dictionarycleanup(self): #Cleanup method written to ensure that the dictionary key and contact name are always matching and the contact name is not changed without changing the dictionary name as well
		bookentries=self.actualdictionary.keys() #Retreives all existing keys from the dictionary
		for item in bookentries: #For each existing key
			cleantest=(item.lower()==self.actualdictionary[item].actualcard[0].fieldname.lower()) #Check if the key matches the name of the contact specified in the name field

			if cleantest==True: #If the field is "clean" (i.e. names match up)
				continue #Continue checking the remaining keys using the loop
			elif cleantest==False: #If they don't match
				cardbuffer=retrievecard(item) #Retrieve the address card using the current key
				self.addcard(cardbuffer) #re-store the address card using the add card method which will copy the contact name as the key when storing the address card
				del self.actualdictionary[item] #delete the old entry with the mistmatching key

	def removecard(self, userspeccardname): #Instance method to remove the specified address card

		deletecheck=self.actualdictionary.haskey(userspeccardname) #Uses the haskey dictionary method to search for the contact in the address book

		if deletecheck==True: #If card exists
			del self.actualdictionary[userspeccardname] #Delete it

		elif deletecheck==False: #If card does not exist
			print
			print 'Sorry. Contact not found' #indicate so to the user 
			print

	def keysearcher(self, userspeckey): #Keysearcher method searches for a specified key in the address book dictionary object (case insensitive)
		allkeys=self.actualdictionary.keys() #Retrieves all the keys in the address book as a list object
		indexcounter=0 #helps to know which index is being accessed
		foundkey='bad' #Initializes the indicator that is returned if no matchign key is found

		for eachkey in allkeys: # retreives each element in the allkeys list object
			test=(eachkey.lower()==userspeckey.lower()) #Checks the key specified by the user against the key retreived from the address book dictionary object
			if test ==True: #If match found
				foundkey=eachkey #save the key
				break #break loop (Assumes only one instance of the contact is found)
			else:
				indexcounter += 1 #Increments the indexcounter
		if foundkey=='bad': #If at the end of the loop, no match is found, return 'bad' to tell the programme that no key was found

			return 'bad'

		else:
			return allkeys[indexcounter] #If match is found, return the key

	def briefallview(self): #Instance method that displays a brief view of only the contact names in the address book
		contactlist=self.actualdictionary.keys() #Retrieves the keys in the address book 
		contactlist.sort() #sorts them in alphabetical order

		#These lines format the display of the address book contacts
		print '-----------------------------------------------------------------------------'
		print 'Displaying contacts in current address book (Brief View):'
		print
		for eachkey in contactlist: #Retreives each key in the list
			print eachkey #Prints it 
		print 
		print '-----------------------------------------------------------------------------'

	def fullallview(self): #Instance method that creates a full view of every field for every contact in the address book
		print '-----------------------------------------------------------------------------'
		contactlist=self.actualdictionary.keys() #Retrieves all keys

		if len(contactlist)==0: #If no contacts are stored, does not enumerate anything and simply indicates no contacts to the user
			print
			print 'NO CONTACTS CONTAINED IN THIS ADDRESS BOOK'
			print

		else:
			contactlist.sort() #Else, it sorts the keys 
			print 'Displaying contacts in current address book (Full View):' #And displays them
			print
			for eachkey in contactlist:
				tempholder=self.actualdictionary[eachkey]
				tempholder.display() #Uses the display instance method defined for address cards to display the full address card
			print 
		print '-----------------------------------------------------------------------------'

	