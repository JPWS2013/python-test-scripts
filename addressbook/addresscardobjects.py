class addresscardobjects:
	'This class allows users to create their own fields in an address card' #Defines the purpose of the addresscardobjects class

	def __init__(self, userspecfieldname='NONE', userspecvalue='NONE'): #Defines the way the class instance should be initiated
		
		try:
			self.fieldname=userspecfieldname #Assigns the field name and value specified by the user to the appropriate instance variables
			self.fieldvalue=userspecvalue 

		except AttributeError: #Tries to catch an exception if the field could not be created
			print 'Unable to create the requested field'
