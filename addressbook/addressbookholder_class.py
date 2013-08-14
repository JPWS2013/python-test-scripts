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

		try:
			instructfilesearch=open('addbookworkfiles/instruct_file', "r")

		except IOError, e:
			print
			print 'Sorry. File not Found:', e
			print

		numberoffiles=instructfilesearch.readline()
		numberoffiles=int(numberoffiles)
		
		instructfilesearch.close()

		for i in range(numberoffiles):
			try:
				filename='addbookworkfiles/addressbook'+str(i+1)
				bookfilesearch=open(filename, "r")
			except IOError, e:
				print 
				print 'Sorry. Unable to retrieve addressbook:', e
				print

			lines=bookfilesearch.readlines()
			numberofcontacts=0
			for line in lines:
				numberofcontacts+=1

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