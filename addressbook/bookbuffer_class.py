from addresscard_class import *
from addressbook_class import *
import sys
import time

class bookbuff:
	def __init__(self, userspecbook):
		self.addbook=userspecbook

	def mainprogramme(self):

		myaddressbook=self.addbook

		submainmenuselect='0' #Variable that stores the main menu selection from the user

		while submainmenuselect!='9': #Ensures the loop is continually run unless user selects 9 (exit option)

			print 'Shown below is a list of actions you may perform:' #Options
			print '1. Add a New Address Card'
			print '2. Modify an Address Card'
			print '3. Display an Address Card'
			print '4. Display address book (Brief View)'
			print '5. Display address book (Full View)'
			print '6. Remove an Address Card'
			print '9. Return to the main menu'
			print ' '

			submainmenuselect=raw_input('Please enter the number corresponding to the action you would like to perform:') #Request for user's choice
			print ' '

			if submainmenuselect=='1': #Option 1 executed
				print 'Welcome to the address card creation wizard' #Welcome message for card creation
				print ' '
				time.sleep(1) #1 second pause of programme
				cardcreation=addresscard() #Initializes an empty address card

				creation_1_option='e' #variables that hold user choices for each step of 
				creation_2_option='e'
				creation_3_option='e'

				while (creation_1_option != 'y') or (creation_1_option!='n'): # Creates a loop in case user does not enter a valid choice for step 1 of address card creation

					creation_1_option=raw_input('Would you like to enter a name? (y/n) ') #Requests a choice from user

					if (creation_1_option.lower()=='y') or (creation_1_option.lower()=='n'):
						break #Breaks the loop if the choice entered by the user is valid (either upper or lower case 'y' or 'n')
					else:
						print 'Choice not recognized. Please try again.' #Tells the user choice not valid and re-loops

				if creation_1_option.lower()=='y': #If user selects this choice either using upper or lower case 'y'
					creation_1=raw_input('Please enter the name of the new contact here: ')#Requests for the desired name
					cardcreation.actualcard[0].fieldvalue=creation_1 #Stores it in the address card object
				
				while (creation_2_option != 'y') or (creation_2_option!='n'): #Creates a loop in case user does not enter a valid choice for step 2 of address card creation

					print
					creation_2_option=raw_input('Would you like to enter  phone number? (y/n) ') #Requests a choice from user

					if (creation_2_option.lower()=='y') or (creation_2_option.lower()=='n'): 
						break #Breaks the loop if the choice entered by the user is valid (either upper or lower case 'y' or 'n')
					else:
						print 'Choice not recognized. Please try again.' #Tells the user choice not valid and re-loops
				

				if creation_2_option.lower()=='y': #If user selects this choice either using upper or lower case 'y'
					creation_2=raw_input('Please enter the phone number of your new contact here: ') #Requests for the contact number to store
					cardcreation.actualcard[1].fieldvalue=creation_2 #Stores it in the address card object

				if cardcreation.actualcard[0].fieldvalue=='NONE': #Checks if a name was specificed

					while (creation_3_option != 'y') or (creation_3_option!='n'): #Starts a loop in case user enters an invalid selection for step 3

						creation_3_option=raw_input('Are you sure you do not want to add a name to this address card? (y/n) ') #Gives the user a second chance to add a name

						if (creation_3_option.lower()=='y') or (creation_3_option.lower()=='n'):
							break #Breaks the loop if user choice is valid as defined above
						else:
							print 'Choice not recognized. Please try again.' #Re-loops if user choice is invalid
					

					if creation_3_option.lower()=='n': #If yes, then no further code is executed. If no, then the programme gives the user a chance to add the name now
						creation_1=raw_input('Please enter the name of the new contact here: ') #Requests the name from the user
						cardcreation.actualcard[0].fieldvalue=creation_1 #stores it in the address card object

				myaddressbook.addcard(cardcreation) #Stores the address card in the address book

				print
				print 'Your address card has been created. Its contents are as follows:'
				print

				cardcreation.display() #Displays the created address card

			elif submainmenuselect=='2': #Code for second option

				retreivedcard='bad'

				while retreivedcard=='bad':
					modify_1_search=raw_input('Please enter the name of the contact you would like to modify or enter "exit" to return to the main menu: ') #Requests for the name of contact to retreive

					if modify_1_search.lower() =='exit': #If user requests to exit
						returntomainmenu=True #send a true to the variable 
						break
					
					else:
						returntomainmenu=False #Else return a false
						retreivedkey=myaddressbook.keysearcher(modify_1_search)

						if retreivedkey=='bad':
							print 
							print 'The contact you entered was not recognized. Please try again...'
							print 
							time.sleep(0.5)
							continue
						else:
							break


				if returntomainmenu==True: #If it's true, then option 2 code should break completely and return to the main menu
					print 
					print 'Returning to the main menu...'
					print 
					time.sleep(0.5)
					continue

				else:

					retreivedcard=myaddressbook.retrievecard(modify_1_search) #Tries to retreive the contact


					if retreivedcard =='bad':
						print 
						print 'Contact not found. Returning to the main menu...'
						print
						time.sleep(0.5)
						continue

					else: 
						print
						print 'Address Card found. Retrieving contents now....'
						time.sleep(2)

					modify_1_search=retreivedcard.actualcard[0].fieldvalue #Sets the name entered by the user to be identical to the key in the address book (in case of case differences)
					submenu_selection='1000' #Sets submenu selection variable to loop parameter

					while submenu_selection != '0': #Starts a loop to continually offer the user actions to perform on an address card

						print ' '
						print 'Below are a list of actions you may perform:'
						print '1. Display Address Card'
						print '2. Create a New Field'
						print '3. Modify an Address Card Field'
						print '4. Delete an Existing Address Card Field'
						print '0. Return to the previous menu'
						print ' '

						submenu_selection=raw_input('Please enter the number corresponding to the action you would like to perform here: ')
						
						if submenu_selection=='1':
							retreivedcard.display()

						if submenu_selection=='2':
							print
							newfield_1=raw_input('Please enter the name of the new field you would like to add: ')
							newfield_2=raw_input('Please enter the information you would like to store in this new field: ')

							retreivedcard.createnewfield(newfield_1, newfield_2)

							print 'The field', retreivedcard.actualcard[-1].fieldname, 'has been created with the value', retreivedcard.actualcard[-1].fieldvalue

						if submenu_selection=='3':
							modifyfield_1=raw_input('Enter the name of the field you would like to modify: ')
							modifyfield_2=raw_input('Enter the new information you would like that field to contain: ')
							retreivedcard.editfield(modifyfield_1, modifyfield_2)

						if submenu_selection=='4':
							print
							modifyfield_1=raw_input('Enter the name of the field you would like to delete: ')
							retreivedcard.deletefield(modifyfield_1)

					print ' '
					print 'You have chosen to return to the main menu. Please wait while pack up operations are performed.'
					del myaddressbook.actualdictionary[modify_1_search]
					myaddressbook.addcard(retreivedcard)
					time.sleep(1)
					print ' '
					print 'Pack up operations are complete. Returning to the main menu....'
					print ' '
					time.sleep(1)

			#elif mainmenuselect=='3':


			elif submainmenuselect=='4':
				myaddressbook.briefallview()

			elif submainmenuselect=='5':
				myaddressbook.fullallview()

			elif submainmenuselect=='6':
				print 
				delete_1=raw_input('Please enter the name of the contact you would like to delete: ')

				foundcontact=myaddressbook.keysearcher(delete_1)

				if foundcontact=='bad':
					print
					print 'Sorry, the contact you with to delete cannot be found'
					print

				else:
					del myaddressbook.actualdictionary[foundcontact]
					print
					print 'Contact has been deleted'
					print

			elif submainmenuselect=='9':
				break

			else:
				print 'Choice not recognized. Please try again.'
				print
				time.sleep(0.5)

		print
		print 'Returning to the Main Menu....'
		print
		return myaddressbook