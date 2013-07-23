from addresscard_class import *
from addressbook_class import *
import sys

myaddressbook=addressbook()

print ' '
print 'Welcome to to the address book programme!'
print ' '

mainmenuselect='0'

while mainmenuselect!='9':

	print 'Shown below is a list of actions you may perform:'
	print '1. Add a New Address Card'
	print '2. Modify an Address Card'
	print ' '

	mainmenuselect=raw_input('Please enter the number corresponding to the action you would like to perform:')
	print ' '

	if mainmenuselect=='1':
		print 'Welcome to the address card creation wizard'
		print ' '
		cardcreation=addresscard()

		creation_1_option='e'
		creation_2_option='e'
		creation_3_option='e'

		while (creation_1_option != 'y') or (creation_1_option!='n'):

			creation_1_option=raw_input('Would you like to enter a name? (y/n) ')

			if (creation_1_option=='y') or (creation_1_option=='n'):
				break
			else:
				print 'Choice not recognized. Please try again.'

		if creation_1_option.lower()=='y':
			creation_1=raw_input('Please enter the name of the new contact here: ')
			cardcreation.actualcard[0].fieldvalue=creation_1
		
		while (creation_2_option != 'y') or (creation_2_option!='n'):

			creation_2_option=raw_input('Would you like to enter  phone number? (y/n) ')

			if (creation_2_option=='y') or (creation_2_option=='n'):
				break
			else:
				print 'Choice not recognized. Please try again.'
		

		if creation_2_option.lower()=='y':
			creation_2=raw_input('Please enter the phone number of your new contact here: ')
			cardcreation.actualcard[1].fieldvalue=creation_2

		if cardcreation.actualcard[0].fieldvalue=='NONE':

			while (creation_3_option != 'y') or (creation_3_option!='n'):

				creation_3_option=raw_input('Are you sure you do not want to add a name to this address card? (y/n) ')

				if (creation_3_option=='y') or (creation_3_option=='n'):
					break
				else:
					print 'Choice not recognized. Please try again.'
			

			if creation_3_option.lower()=='n':
				creation_1=raw_input('Please enter the name of the new contact here: ')
				cardcreation.actualcard[0].fieldvalue=creation_1

		myaddressbook.addcard(cardcreation)

		print 'Your address card has been created. Its contents are as follows:'

		cardcreation.display()

	if mainmenuselect=='2':

		retreivedcard='bad'

		while retreivedcard=='bad':

			modify_1_search=raw_input('Please enter the name of the contact you would like to modify: ')
			retreivedcard=myaddressbook.retrievecard(modify_1_search)

			if retreivedcard !='bad':
				print 'Address Card found.'
				break

		submenu_selection='1000'

		while submenu_selection != '0':

			print ' '
			print 'Below are a list of actions you may perform:'
			print '1. Display Address Card'
			print '2. Create a New Field'
			print '3. Modify an Address Card Field'
			print '4. Delete an Existing Address Card Field'
			print '0. Return to the main menu'
			print ' '

			submenu_selection=raw_input('Please enter the number corresponding to the action you would like to perform here: ')

			if submenu_selection=='1':
				retreivedcard.display()

			if submenu_selection=='2':
				newfield_1=raw_input('Please enter the name of the new field you would like to add: ')
				newfield_2=raw_input('Please enter the information you would like to store in this new field: ')

				retreivedcard.createnewfield(newfield_1, newfield_2)

				print 'The field', retreivedcard.actualcard[-1].fieldname, 'was created with the value', retreivedcard.actualcard[-1].fieldvalue

			if submenu_selection=='3':
				modifyfield_1=raw_input('Enter the name of the field you would like to modify: ')
				modifyfield_2=raw_input('Enter the new information you would like that field to contain: ')
				retreivedcard.editfield(modifyfield_1, modifyfield_2)

			if submenu_selection=='4':
				modifyfield_1=raw_input('Enter the name of the field you would like to delete: ')
				retreivedcard.deletefield(modifyfield_1)

		print ' '
		print 'You have chosen to return to the main menu. Please wait while pack up operations are performed.'
		del myaddressbook.actualdictionary[modify_1_search]
		myaddressbook.addcard(retreivedcard)
		print ' '
		print 'Pack up operations are complete. Returning to the main menu....'
		print ' '

sys.exit('You have chosen to exit the programme. Thank you and have a nice day.')