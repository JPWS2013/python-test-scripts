#Import the relevant modules for class definitions and the sys, time and os modules
from addresscard_class import *
from addressbookholder_class import *
from bookbuffer_class import *
import sys #Needed for ending the programme
import time #Needed for the pauses in the programme running
from endprogops import *
import os #Needed for manipulating the text files when opening or closing the programme

myaddressbookholder=addressbookholder() #Initializes an empty address book library

myaddressbookholder.openprogops() #Retreives any existing address books

#This big block simply clears the screen to make the command line more visually acceptable
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print 'Welcome to to the address book programme!' 
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '

time.sleep(2) #A pause after the welcome message
mainmenuselect='0' #Sets the mainmenuselect to a number that doesn't exist in the list
packingfunction=False #Sets the packing function to false so that the loop continues until it is changed to true (indicating user wants to leave the programme)

while packingfunction==False: #Loops through the options menu until a valid selection is made 

	#This displays a list of all options available to the user

	print 'A list of available actions is shown below:'
	print 
	print '1. Create a New Address Book'
	print '2. View all Address Books'
	print '3. View 1 specific Address Book'
	print '4. Rename Address Book'
	print '5. Retrieve a specific address book to edit'
	print '6. Perform a global search on all address books'
	print '7. Delete an Address Book'
	print '9. Exit the Programme'
	print 

	mainmenuselect=raw_input('Please enter the number corresponding to the action you would like to perform: ') #Ask for the user's choice of action
	print #Leaves a 1-line gap

#-------------------------------------------------------------
#Code for first action choice begins here
#-------------------------------------------------------------

	if mainmenuselect=='1': #If user selects action 1 (create new address book)

		bookcreation_2='f' #Presets bookcreation_2 to a non-existant letter to start the loop

		while bookcreation_2.lower() != 'y': #While the user is not satisfied with the name he has entered

			bookcreation_1=raw_input('Please enter the name of your new address book: ') #Asks for the name of the addres book
			print 
			print 'Your new address book will be named: ', bookcreation_1 #Confirms what the user typed
			print
			bookcreation_2=raw_input('Is this the correct name? (y/n) ') #Asks for confirmation from user
			print

			if bookcreation_2.lower()=='y': #If user agrees that it is right 
				break #break from the loop

		print 'Creating your address book now. Please wait...' #Indicates address book is being created

		bookbuffer=addressbook(bookcreation_1) #Creates a buffer in which to contain the new address book 
		myaddressbookholder.createbook(bookbuffer) #Adds the address book to library 
		time.sleep(1) #Waits for 1 second 

		print
		print 'Your address book has been created successfully' #Sends confirmation to the user
		print
		time.sleep(1) #Waits for 1 second

#---------------------------------------------------------------------
#Code for second action choice begins here
#---------------------------------------------------------------------

	if mainmenuselect=='2': #If user selects 2 (View all address books)
		print 
		print '------------------------------------------------------------------------' #Formatting for display of address book list view
		print
		holderkeys=myaddressbookholder.library.keys() #Retreives the keys for each address book from the library into a list

		if len(holderkeys)==0: #If there are no address books stored
			print 'NO ADDRESS BOOKS FOUND' #Indicate no address books found to the user

		else:
			print 'The names of the Address Books you have are:' #Formatting for address book list view
			print
			myaddressbookholder.viewallbooks() #Calls the viewallbooks function to list the names of all books with enumeration

		print
		print '-------------------------------------------------------------------------' #Formatting for display of address book list view

#-------------------------------------------------------------------
#Code for third action choice begins here
#-------------------------------------------------------------------

	if mainmenuselect=='3': #If user selects 3 (View 1 specific address book)

		addressbookview_1=False #Keeps the loop going until user chooses to go back or an address book is found

		keyscheck=myaddressbookholder.library.keys() #Collects a list of all keys of addressbooks in the library

		if len(keyscheck)==0: #Checks if no addressbooks are stored
			print 
			print 'NO ADDRESS BOOKS FOUND IN THIS LIBRARY' #Indicates this to user
			print 
			print 'Returning to the main menu...' #Indicates it is returning to the main menu
			print
			time.sleep(0.5) #0.5sec wait before returning

		else:	#If there are address books stored
			while addressbookview_1 !=True: #Loop will continue until user hits go back or an address book is found

				print #Leaves a line gap
				addressbookview_1=raw_input('Please enter the name of the address book you would like to view or enter "go back" to return to the main menu: ')#Requests for the name of the address book or go back to return

				if addressbookview_1.lower()=='go back': #If the user enters go back in upper or lower case 
					addressbookview_1=True #System returns true
					break #Loop is broken
				else:
					addressbookview_2 = myaddressbookholder.keysearcher(addressbookview_1) #Calls the key searcher to check if the addressbook exists
					
					if addressbookview_2 == 'bad': #If the searcher returns bad, it means it couldn't find the address book
						print 
						print 'Sorry. The address book you requested could not be found. Please try again.' #Indicates this to user
						print
						continue #Continues back through the loop to allow the user to try again
					
					else: #If the searcher does not return bad, it should have found the address book
						break #Therefore, break the loop

			if addressbookview_1==True: #If addressbookview_1 is True, it means the user entered go back
				print
				print'Returning to the main menu...' #Therefore, indicate this to user
				time.sleep(1) #Wait 1 second
				print
				#After this, it skips to the end of the loop and returns to the main menu
		
			else: #If addressbookview_1 is not true, then it means that it broke the loop because an addressbook was found
				print #Leaves a gap
				bookbuffer=myaddressbookholder.library[addressbookview_2] #Adds the addressbook to a buffer to create an addressbook object
				bookbuffer.fullallview() #Calls the instance method to display the full address book
				print #Leaves a gap
				spacegiver=raw_input('When ready to return to the main menu, hit the enter key') #Holds the programme until the user is ready to continue by hitting the enter key
				#Note that nothing is done with the user input collected above. It is merely used as a stopper
				print #Leaves a gap
				print 'Returning to the main menu...' #Indicates it is returning to the main menu
				time.sleep(1) #Waits for 1 second
				print #Leaves a gap

#--------------------------------------------------------------------
#Code for fourth action choice begins here
#--------------------------------------------------------------------

	if mainmenuselect=='4': #If user selects 4 (Rename an address book)
		keyscheck=myaddressbookholder.library.keys() #Retreives all keys for stored address books

		if len(keyscheck)==0: #Checks if any address books are stored
			print 
			print 'NO ADDRESS BOOKS FOUND IN THIS LIBRARY' #Indicates that none are stored
			print 
			print 'Returning to the main menu...' #Indicates returning to main menu
			print
			time.sleep(0.5) #0.5second wait before returning

		else: #If address books are stored

			namechange_1=False #Initiates the variable that will keep the loop goign until an address book is found or user enters go back

			while namechange_1 !=True: #While the user has not entered go back
				namechange_1=raw_input('Please enter the name of the address book you would like to change or enter "go back" to return to the main menu: ') #Requests for the address book to change

				if namechange_1.lower()=='go back': #If the user enters go back
					namechange_1=True #Change the namechange_1 variable to True
					break #Break the loop
				else: #If user did not enter go back

					namechange_2=myaddressbookholder.keysearcher(namechange_1) #Search for the specified key

					if namechange_2=='bad': #If the searcher returns bad
						print
						print'The address book you have requested could not be found. Please try again' #Indicate to user no match found
						print
						continue #Go back through the loop to give the user another chance 

					else:
						break #Else, it must have found the addressbook so break the loop
						

			if namechange_1==True: #If the user entered go back
				print
				print 'Returning to the main menu...' #Indicate returning to the main menu
				print
				time.sleep(0.5) #Wait 0.5sec
				#After this, it skips the rest of the code and returns to the main menu
			else: #If not true, then that means it broke out of loop when it found an address book
				
				namechange_4='n' #Presets the namechange_4 variable to keep in the loop until user is satisfied with new name

				while namechange_4.lower()!='y': #Loop to ensure user is satisfied with new name
					print #Leaves a gap
					namechange_3=raw_input('Enter the new name of your address book here: ') #Requests for the new name of the address book
					print
					print 'The new name of your address book will be: ', namechange_3 #Returns the name entered by the user for confirmation
					print
					namechange_4=raw_input('Is this correct? (y/n): ') #Asks for confirmation from user

					if namechange_4.lower()=='y': #If user enters 'y', case insensitive
						print
						print'Please wait, updating records now...' #Indicates that operation being done

						addressbookbuffer=myaddressbookholder.library[namechange_2] #Adds the existing address book to a buffer
						addressbookbuffer.bookname=namechange_3 #Reassigns the book name to the new one
						del myaddressbookholder.library[namechange_2] # Deletes the old address book from the library
						myaddressbookholder.createbook(addressbookbuffer) #Re-adds the new one with the new name to the library

						time.sleep(1) #Pauses the programme for 1 sec

						print'Update completed successfully. Returning to the main menu....' #Indicates it is returning to the main menu
						time.sleep(0.5) #Pauses the programme for 0.5sec
						print #Leaves a gap
						break #Breakes the loop since operation complete
					
					else:
						continue #If not 'y', means user not satisfied, go back through the loop again

#----------------------------------------------------------------------
#Code for fifth action choice begins here
#----------------------------------------------------------------------

	if mainmenuselect=='5': #If user selects 5(Retreive a specific address book to edit)
		addressbookretreive_1=False #Same variable to stay within the loop until user enters go back

		keyscheck=myaddressbookholder.library.keys() #Same code to retreive keys

		if len(keyscheck)==0: #Same code to check if there are any address books stored at all
			print 
			print 'NO ADDRESS BOOKS FOUND IN THIS LIBRARY'
			print 
			print 'Returning to the main menu...'
			print
			time.sleep(0.5)

		else:	
			while addressbookretreive_1 !=True: #Same loop to allow go back functionality

				print
				addressbookretreive_1=raw_input('Please enter the name of the address book you would like to view or enter "go back" to return to the main menu: ') #Asks user for the name of the address book they would like to edit

				if addressbookretreive_1.lower()=='go back': #If user enters go back
					addressbookviewretreive_1=True #Change the variable to True
					break #Break the loop
				else: #If not
					addressbookretreive_2 = myaddressbookholder.keysearcher(addressbookretreive_1) #Search for the addressbook specified by user
					if addressbookretreive_2 == 'bad': #If searcher returns 'bad', means no book found
						print 
						print 'Sorry. The address book you requested could not be found. Please try again.' #Indicates this to users
						print
						continue #Goes back through the loop to allow the user to try again
					else:
						break #If does not return 'bad', means it found an addressbook

			if addressbookretreive_1==True: #If the variable is true, means user entered 'go back'
				print
				print'Returning to the main menu...' #Indicate to user
				time.sleep(1)
				print
				#After this, it skips the rest of the script and returns to the main menu
			else: #If not means loop ended because book was found
				print
				bufferforbook=myaddressbookholder.library[addressbookretreive_2] #Stores the address book in a buffer
				bufferforediting=bookbuff(bufferforbook) #Creates a bookbuff object 

				buffer_postediting=bufferforediting.mainprogramme() #Enters the subprogramme that handles the address book and address cards

				#When the subprogramme exits, it returns the modified version of the addressbook to the variable buffer_postediting

				del myaddressbookholder.library[addressbookretreive_2] #Delets the old copy of address book 
				myaddressbookholder.createbook(buffer_postediting) #Adds the new one to the library
				
				time.sleep(1) #1 sec delay before returning to main menu

#----------------------------------------------------------------------
#Code for sixth action choice begins here
#----------------------------------------------------------------------

	if mainmenuselect=='6': #If user selects 5(Perform a global search on all address books)

		keyschecker=myaddressbookholder.library.keys() #Same code to retreive all keys from dictionary

		if len(keyschecker)==0: #Same code to check for no address books stored
			print 
			print 'NO ADDRESS BOOKS TO SEARCH'
			print 
			print 'Returning to the main menu...'
			print
			time.sleep(0.5)

		else: 
			contactfound=[] #Creates a list to store any contact it finds
			bookfoundin=[] #Creates  a list to store the address book it found the contact in
			globalsearch_1_check=False #Variable to keep the loop going unless user enters go back
			print
			globalsearch_1=raw_input('Please enter the contact you would like to search for or enter "go back" to return to the main menu: ') #Requests the user to enter the name of the contact they are searching for

			if globalsearch_1.lower()=='go back':#If user enters go back
				globalsearch_1_check=True #Changes the gariable to True

			if globalsearch_1_check==True: #If the variable is True
				print
				print'Returning to the main menu...' #Indicates returning to main menu
				time.sleep(1)
				print
		
			else: #If variable not true, then user did not enter go back

				# alladdressbookkey=myaddressbookholder.library.keys() #Retreives all the keys

				# for eachKey in alladdressbookkey: #for each key
				# 	eachBook=myaddressbookholder.library[eachKey] #Retreives each addressbook
				# 	globalsearchresult=eachBook.keysearcher(globalsearch_1) #Searches for a contact in the address book
				
				# 	if globalsearchresult != 'bad': #If the result is not 'bad', means something was found
				# 		contactfound.append(globalsearchresult) #contact name stored
				# 		bookfoundin.append(eachBook.bookname) #Book it was found in stored
				
				contactfound=myaddressbookholder.globalsearch(globalsearch_1)

				if len(contactfound)==0: #If the length of contactfound is zero, nothing found
					print 
					print 'Sorry. Your specified contact was not found in any of your existing addressbooks.' #Indicate to user
					print
					print 'Returning to the main menu....'
					print
					time.sleep(0.5)

				else: #Else print them all out
					print 
					print 'There were ', len(contactfound), 'contact(s) found that match the name you specified. They are shown below:'

					for eachContact in contactfound:
						contactbuffer=myaddressbookholder.library[eachContact[1]].actualdictionary[eachContact[0]] #Retreives the address card from the address book
						#print 
						#print 'From Address Book: ', bookfoundin[enumerator]
						contactbuffer.display()
						#print

					print
					waitingholder=raw_input('Once done, hit the enter key to return to the main menu.')
					print
					print 'Returning to the main menu....'
					print
					time.sleep(0.5)
	
	if mainmenuselect=='7':
		deletebook_1_check=False

		keyscheck=myaddressbookholder.library.keys()

		if len(keyscheck)==0:
			print 
			print 'NO ADDRESS BOOKS AVAILABLE FOR DELETION'
			print 
			print 'Returning to the main menu...'
			print
			time.sleep(0.5)

		else:	
			while deletebook_1_check !=True:

				print
				deletebook_1=raw_input('Please enter the name of the address book you would like to delete or enter "go back" to return to the main menu: ')

				if deletebook_1.lower()=='go back':
					deletebook_1_check=True
					break
				else:
					print
					deletebook_2=raw_input('Are you sure you wish to delete this address book? (y/n): ')

					if deletebook_2.lower()=='n':
						continue
					elif deletebook_2.lower()=='y':

						deletebook_2 = myaddressbookholder.keysearcher(deletebook_1)
						if deletebook_2 == 'bad':
							print 
							print 'Sorry. The address book you requested could not be found. Please try again.'
							print
							continue
						else:
							break

			if deletebook_1_check==True:
				print
				print'Returning to the main menu...'
				time.sleep(1)
				print
		
			else:


				myaddressbookholder.deletebook(deletebook_2)
				print
				print 'Returning to the main menu....'
				print
				time.sleep(0.5)

	if mainmenuselect=='9':
		print 
		print 'You have chosen to exit the system. Please wait while packing opertions are performed...'
		print 

		directory='addbookworkfiles'
		filelist=os.listdir(directory)

		for bookFile in filelist:
			os.remove(directory + "/" + bookFile)
	
		packingfunction=myaddressbookholder.endprogops()

		time.sleep(1)

		if packingfunction==True:
			print 
			print'Operations completed successfully'
			break
		else:
			print 
			print 'Operation failed. Please try again'
			print

	else:
		print
		print 'You have entered an invalid choice. Please try again.'
		print 


sys.exit('You have chosen to exit the programme. Thank you and have a nice day.')