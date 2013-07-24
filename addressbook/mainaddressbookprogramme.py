from addresscard_class import *
from addressbookholder_class import *
from bookbuffer_class import *
import sys
import time

myaddressbookholder=addressbookholder()

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
print 'Welcome to to the address book programme!' #Welcome message displayed at the start of programme
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '
print ' '

time.sleep(2) #2 second pause in programme
mainmenuselect='0' #Variable that stores the main menu selection from the user

while mainmenuselect!='9':

	print 'A list of available actions is shown below:'
	print 
	print '1. Create a New Address Book'
	print '2. View all Address Books'
	print '3. View 1 specific Address Book'
	print '4. Rename Address Book'
	print '5. Retrieve a specific address book to edit'
	#print '6. Perform a global search on all address books'
	#print '7. Delete an Address Book'
	print '9. Exit the Programme'
	print 

	mainmenuselect=raw_input('Please enter the number corresponding to the action you would like to perform: ')
	print

	if mainmenuselect=='1':

		bookcreation_2='f'

		while bookcreation_2.lower() != 'y':

			bookcreation_1=raw_input('Please enter the name of your new address book: ')
			print 
			print 'Your new address book will be named: ', bookcreation_1
			print
			bookcreation_2=raw_input('Is this the correct name? (y/n) ')
			print

			if bookcreation_2.lower()=='y':
				break

		print 'Creating your address book now. Please wait...'

		bookbuffer=addressbook(bookcreation_1)
		myaddressbookholder.createbook(bookbuffer)
		time.sleep(1)

		print
		print 'Your address book has been created successfully'
		print
		time.sleep(1)

	if mainmenuselect=='2':
		print 
		print '------------------------------------------------------------------------'
		print
		holderkeys=myaddressbookholder.library.keys()

		if len(holderkeys)==0:
			print 'NO ADDRESS BOOKS FOUND'

		else:
			print 'The names of the Address Books you have are:'
			print
			holderkeys.sort()
			bookenumerator=1
			for eachKey in holderkeys:
				print bookenumerator,'. ', eachKey
				bookenumerator += 1
		print
		print '-------------------------------------------------------------------------'

	if mainmenuselect=='3':

		addressbookview_1=False

		keyscheck=myaddressbookholder.library.keys()

		if len(keyscheck)==0:
			print 
			print 'NO ADDRESS BOOKS FOUND IN THIS LIBRARY'
			print 
			print 'Returning to the main menu...'
			print
			time.sleep(0.5)

		else:	
			while addressbookview_1 !=True:

				print
				addressbookview_1=raw_input('Please enter the name of the address book you would like to view or enter "go back" to return to the main menu: ')

				if addressbookview_1.lower()=='go back':
					addressbookview_1=True
					break
				else:
					addressbookview_2 = myaddressbookholder.keysearcher(addressbookview_1)
					if addressbookview_2 == 'bad':
						print 
						print 'Sorry. The address book you requested could not be found. Please try again.'
						print
						continue
					else:
						break

			if addressbookview_1==True:
				print
				print'Returning to the main menu...'
				time.sleep(1)
				print
		
			else:
				print
				bookbuffer=myaddressbookholder.library[addressbookview_2]
				bookbuffer.fullallview()
				print
				spacegiver=raw_input('When ready to return to the main menu, hit the enter key')
				print
				print 'Returning to the main menu...'
				time.sleep(1)
				print
	if mainmenuselect=='4':
		keyscheck=myaddressbookholder.library.keys()

		if len(keyscheck)==0:
			print 
			print 'NO ADDRESS BOOKS FOUND IN THIS LIBRARY'
			print 
			print 'Returning to the main menu...'
			print
			time.sleep(0.5)

		else:

			namechange_1=False
			while namechange_1 !=True:
				namechange_1=raw_input('Please enter the name of the address book you would like to change or enter "go back" to return to the main menu: ')

				if namechange_1.lower()=='go back':
					namechange_1=True
					break
				else:

					namechange_2=myaddressbookholder.keysearcher(namechange_1)

					if namechange_2=='bad':
						print
						print'The address book you have requested could not be found. Please try again'
						print
						continue

					else:
						break
						

			if namechange_1==True:
				print
				print 'Returning to the main menu...'
				print
				time.sleep(0.5)

			else:
				namechange_4='n'

				while namechange_4.lower()!='y':
					print
					namechange_3=raw_input('Enter the new name of your address book here: ')
					print
					print 'The new name of your address book will be: ', namechange_3
					print
					namechange_4=raw_input('Is this correct? (y/n): ')

					if namechange_4.lower()=='y':
						print
						print'Please wait, updating records now...'

						addressbookbuffer=myaddressbookholder.library[namechange_2]
						addressbookbuffer.bookname=namechange_3
						del myaddressbookholder.library[namechange_2]
						myaddressbookholder.createbook(addressbookbuffer)

						time.sleep(1)

						print'Update completed successfully. Returning to the main menu....'
						time.sleep(0.5)
						print
						break
					
					else:
						continue

	if mainmenuselect=='5':
		addressbookretreive_1=False

		keyscheck=myaddressbookholder.library.keys()

		if len(keyscheck)==0:
			print 
			print 'NO ADDRESS BOOKS FOUND IN THIS LIBRARY'
			print 
			print 'Returning to the main menu...'
			print
			time.sleep(0.5)

		else:	
			while addressbookretreive_1 !=True:

				print
				addressbookretreive_1=raw_input('Please enter the name of the address book you would like to view or enter "go back" to return to the main menu: ')

				if addressbookretreive_1.lower()=='go back':
					addressbookviewretreive_1=True
					break
				else:
					addressbookretreive_2 = myaddressbookholder.keysearcher(addressbookretreive_1)
					if addressbookretreive_2 == 'bad':
						print 
						print 'Sorry. The address book you requested could not be found. Please try again.'
						print
						continue
					else:
						break

			if addressbookretreive_1==True:
				print
				print'Returning to the main menu...'
				time.sleep(1)
				print
		
			else:
				print
				bufferforbook=myaddressbookholder.library[addressbookretreive_2]

				bufferforediting=bookbuffer()

				print bufferforediting.__class__.__name__
				print bufferforbook.__class__.__name__

				bufferforediting.addbook=bufferforbook

				buffer_postediting=bufferforediting.mainprogramme()

				del myaddressbookholder.library[addressbookretreive_2]
				myaddressbookholder.createbook(buffer_postediting)
				
				time.sleep(1)

				




sys.exit('You have chosen to exit the programme. Thank you and have a nice day.')