from addresscardobjects import * #Imports the class and method definitions for the addresscardobjects class

class addresscard:
	'This class creates an object which stores personal information in an address card which may be retrieved later. Its partner class is the addressbook class' #Description of class

	def __init__(self, userspecname='NONE', userspeccp='NONE'): #Defines how the class should be initialized
		'Creates a new address card with at least name and cell phone number instance variables'

		self.actualcard=[] #Creates the list object that will store the fields a user might create within an address card

		fieldholder=addresscardobjects('Name', userspecname) #Creates a name field for storing the contact's name, regardless of whether the user wants it or not (Needed for creating addressbook keys)
		self.actualcard.append(fieldholder) #adds the created field to the address card

		fieldholder=addresscardobjects('Mobile Phone Number', userspeccp) #Automatically creates a mobile phone number field, regardless of whether the user wants it or not (Assumed to be the most likely reason for adding a contact)
		self.actualcard.append(fieldholder) #Adds the created field to the address card

		#print 'Address Card created for', self.actualcard[0].fieldvalue

	def display(self): #Instance method for displaying the contents of the address card including all fields created by the user
		print '----------------------------------------------------------------------------'
		print 'Displaying address card for:', self.actualcard[0].fieldvalue
		print ' '
		
		for item in self.actualcard: #Iteration to print each field in a seperate line
			print item.fieldname, ':', item.fieldvalue

		print ' '
		print '----------------------------------------------------------------------------'

	def createnewfield(self, userspecname='NONE', userspecvalue='NONE'): #Instance method for creating a new custom field
		fieldholder=addresscardobjects(userspecname, userspecvalue) #Creates a new addresscardobjects object
		self.actualcard.append(fieldholder) #Adds the field to the address card

		# print ' '
		# print self.actualcard[-1].fieldname, 'has been created with value:', self.actualcard[-1].fieldvalue #Confirmation of addition of field displayed to user
		# print ' '

	def deletefield(self, userspecname): #Instance method for deleting a field
		
		foundindex=self.fieldsearcher(userspecname) #Employs the field searcher instance method to search for the field the user wants to delete (Returns a list whose first element is "True" if a field was found)

		if foundindex[0]==True: #Checks if a field was found by checking the first element of that list

			del self.actualcard[foundindex[1]] #Performs the deletion
			print
			print 'Entry successfully removed' #Confirms the deletion
			print ' '

		else:

			print 'Sorry. Entry not found' #Indicates to the user that the field they wanted to delete could not be found
			print ' '

	def editfield(self, userspecname, userspecvalue): #Instance method for editing a field

		foundindex=self.fieldsearcher(userspecname) #Searches for the field specified by the user using the fieldsearcher instance method

		if foundindex[0]==True: #If a field was found, 
			self.actualcard[foundindex[1]].fieldvalue=userspecvalue #change the field value to the one specified by the user

			print self.actualcard[foundindex[1]].fieldname, 'has been changed. It is now:', self.actualcard[foundindex[1]].fieldvalue #Print a confirmation that change was made

		elif foundindex[0]==False: #If field was not found, 

			print 'Sorry. Entry not found' #indicate so to the user 

	def renamefield(self, userspecoldname, userspecnewname): #Instance method for renaming fields

		foundindex=self.fieldsearcher(userspecoldname) #Searches for the specified field using the field searcher instance method

		if foundindex[0]==True: #If the field was found, 
			self.actualcard[foundindex[1]].fieldname=userspecnewname #Change the field name to the one specified by the user

			print self.actualcard[foundindex[1]].fieldname, 'has been changed.' #Print a confirmation that change was completed

		elif foundindex[0]==False: #If the field specified could not be found, 
			print 'Sorry. Entry not found' #indicate so to the user

	def fieldsearcher(self, userspecname): #Instance method to search for a field and return the properties needed to retreive it later
		indexcounter=0 #Creates an index counter that corresponds to the index being searched in the list of fields in the address card

		for item in self.actualcard: #Searches through each field in the address card
			searchtest=(item.fieldname.lower() == userspecname.lower()) #Checks the specified field name against the field name of the field (Case-insensitive); Returns true if a field matches

			if searchtest==True: #If a field match is found
				return [searchtest, indexcounter] #Return the logic output and the index of the field in the list as a list object for the programme to make use of the information
				break #Break the loop (Assumes only one instance of a field of the specified name is created)
			else:
				indexcounter +=1 #If no field is found, increment the index counter to the next index

		if searchtest!=True: #If field not found,
			return [False] #return a false to indicate field not found