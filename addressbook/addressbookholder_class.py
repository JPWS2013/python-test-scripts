from addressbook_class import *
import time

class addressbookholder:
	'This class stores a collection of address books'
	
	def __init__(self):
		self.library={}

	def createbook(self, userspecbook):
		self.library[userspecbook.bookname]=userspecbook

	def viewallbooks(self):

		keybuffer=self.library.keys()
		keybuffer.sort()
		bookenumerator=1
		for eachKey in keybuffer: #Iterate through each  key in the list
			print bookenumerator,'. ', eachKey #Print the item number, followed by the key itself
			bookenumerator += 1 #Increment the counter to the next number
		#for eachKey in keybuffer:
			#print eachKey

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

	def endprogops(self):
		
		try:
			allkeys=self.library.keys()

			numberoffiles=len(allkeys)

			instructionalfile=open('addbookworkfiles/instruct_file', "w")

			instructionalfile.write(str(numberoffiles))

			instructionalfile.close()

			for file_enumerator in range(0, (numberoffiles)):
				filenumber=str(file_enumerator+1)
				filename='addbookworkfiles/addressbook'+filenumber
				addbookfile=open(filename, "w")

				addbookbuffer=self.library[allkeys[file_enumerator]]

				filename=addbookbuffer.bookname + ';' + '\n'

				addbookfile.write(filename)

				cardkeys=addbookbuffer.actualdictionary.keys()

				for eachCard in cardkeys:
					cardbuffer=addbookbuffer.actualdictionary[eachCard]

					linetowrite=' '

					for i in range(len(cardbuffer.actualcard)):
						fieldholder=str(cardbuffer.actualcard[i].fieldname)+ ':' + str(cardbuffer.actualcard[i].fieldvalue)
						linetowrite=linetowrite+ fieldholder + ','

					linetowrite=linetowrite+ ';' + '\n'
					addbookfile.write(linetowrite)
				addbookfile.close()
			return True
		except IOError, e:
			return False

	def openprogops(self):
		
		def stringretreiver(stringtosearch, searchcharacter, startpoint=0):
			for stringlength in range(startpoint, len(stringtosearch)):
				characterholder=stringtosearch[stringlength]
				if characterholder==searchcharacter:
					#stoppingpoint=stringlength
					break

			teststring=stringtosearch[stringlength+1]

			if teststring==';':
			 	testresult=True
			else:
			 	testresult=False

			return [stringtosearch[(startpoint+1):stringlength], stringlength, testresult]

		try: #Exception handling code in case instruct_file doesn't exist
			instructfilesearch=open('addbookworkfiles/instruct_file', "r") #Try to open the instruct_file

		except IOError, e: #If you can't open it, indicate so
			print
			print 'We were unable to find the required files. Creating  new address book library now...'
			print
			time.sleep(1)
			return False

		numberoffiles=instructfilesearch.readline() #read the indicated number of files
		numberoffiles=int(numberoffiles) #Convert the number of files to an integer number
		


		instructfilesearch.close() #Close the file

		if numberoffiles==0: #If the number is zero, 
			print
			print 'No prior addressbooks found. Creating a new library now..' #indicate this to user
			print

			time.sleep(1) #wait 1 second

			return False


		for i in range(numberoffiles): #for each file indicated

			try: #exception handling code in case addressbook can't be found
				filename='addbookworkfiles/addressbook'+str(i+1) #open the addressbook file
				bookfilesearch=open(filename, "r") #Open the addressbook file
			except IOError, e:
				print 
				print 'Sorry. Unable to retrieve addressbook:', e
				print
				return False

			lines=bookfilesearch.readlines() #Read all lines in the addressbook
			numberofcontacts=0 #iniitalize the number of contacts to zero
			for line in lines: #for each line in the file
				numberofcontacts+=1 #increment the numberofcontacts to count how many contcts there are

			#numberofcontacts=linecounter-1
			#print 'numberofcontacts=', numberofcontacts
			
			bookname_rawstring=lines[0]
			for stringindex in range(len(bookname_rawstring)):
				characterholder=bookname_rawstring[stringindex]
				if characterholder==';':
					#stoppingpoint=stringlength
					break



			bookname_clean=bookname_rawstring[0:stringindex]
			#booknamesearcher=stringretreiver(lines[0], ';')
			addressbookbuffer=addressbook(bookname_clean)
			#print bookname_clean
			#print len(bookname)

			for eachContact in range(1, numberofcontacts):

				contactline=lines[eachContact] # Name:John,Mobile Phone Number:920282672,;
		 		retreiveroutput= stringretreiver(contactline, ':')
				namefieldname=retreiveroutput[0]#contactline[1:point]
				point=retreiveroutput[1]
				#print namefieldname
				#print 'namefieldname=', namefieldname
				#print retreiveroutput[2]
				

				retreiveroutput= stringretreiver(contactline, ',', point)
				namefieldvalue=retreiveroutput[0]
				point=retreiveroutput[1]
				#print 'namefieldvalue=', namefieldvalue
				#print retreiveroutput[2]

				retreiveroutput= stringretreiver(contactline, ':', point)
				cpfieldname=retreiveroutput[0]
				point=retreiveroutput[1]
				#print 'cpfieldname=', cpfieldname
				#print retreiveroutput[2]

				# for stringlength in range(point, len(contactline)):
				# 	characterholder=contactline[stringlength]
				# 	if characterholder==',':
				# 		point2=stringlength
				# 		break
				retreiveroutput= stringretreiver(contactline, ',', point)
				cpfieldvalue=retreiveroutput[0]
				point=retreiveroutput[1]
				#print 'cpfieldvalue=', cpfieldvalue

				testresult=retreiveroutput[2]
				#print retreiveroutput[2]

				addresscardbuffer=addresscard(namefieldvalue, cpfieldvalue)

				if testresult==True:
					addressbookbuffer.addcard(addresscardbuffer)
					continue

				elif testresult==False:

					while testresult==False:
						retreiveroutput= stringretreiver(contactline, ':', point)
						fieldname=retreiveroutput[0]#contactline[1:point]
						point=retreiveroutput[1]
						#print 'fieldname=', fieldname
						#print retreiveroutput[2]
				

						retreiveroutput= stringretreiver(contactline, ',', point)
						fieldvalue=retreiveroutput[0]
						point=retreiveroutput[1]
						#print 'fieldvalue=', fieldvalue
						testresult=retreiveroutput[2]

						addresscardbuffer.createnewfield(fieldname, fieldvalue)

					addressbookbuffer.addcard(addresscardbuffer)
					continue
			#addressbookbuffer.fullallview()			
			self.createbook(addressbookbuffer)
		return True


	def globalsearch(self, userspeckey):
		#searchedstring_counter=0
		#serchstring_counter=0
		foundkeys=[]
		allbooks=self.library.keys()

		for eachBook in allbooks:
			retrievedbook=self.library[eachBook]

			allkeys=retrievedbook.actualdictionary.keys()

			for eachKey in allkeys:
				print eachKey
				searchedstring_counter=0
				char_test2=False

				while char_test2==False:

					searchstring_counter=0

					#print 'searchedstring_counter==(len(userspeckey))=', searchedstring_counter==(len(userspeckey))
					#print 'char_test2==False = ', char_test2==False
					if (searchedstring_counter==(len(eachKey))) and (char_test2==False):
						break
					
					#print 'eachKey[searchedstring_counter]=', eachKey[searchedstring_counter]
					#print 'userspeckey[searchstring_counter]=', userspeckey[searchstring_counter]

					char_test1=eachKey[searchedstring_counter].lower()==userspeckey[searchstring_counter].lower()

					#print 'char_test1=', char_test1

					if char_test1==True:
						endindex=searchedstring_counter+len(userspeckey)
						testkey=eachKey[searchedstring_counter : endindex]

						#print 'testkey.lower()=', testkey.lower()
						#print 'length=',  len(testkey.lower())
						#print 'userspeckey.lower()=', userspeckey.lower()
						#print 'length=', len(userspeckey.lower())

						char_test2=(testkey.lower()==userspeckey.lower())
						#print 'char_test2=', char_test2
						#print 'char_test2==True =', char_test2==True 

						if char_test2==True:
							foundkeys.append([eachKey, eachBook])
							break

					searchedstring_counter+=1

		return foundkeys	