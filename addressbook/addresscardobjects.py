class addresscardobjects:
	'This class allows users to create their own fields in an address card'

	def __init__(self, userspecfieldname='NONE', userspecvalue='NONE'):
		
		try:
			self.fieldname=userspecfieldname
			self.fieldvalue=userspecvalue

		except AttributeError:
			print 'Unable to create the requested field'
