from addresscard_class import *
from addressbookholder_class import *
from bookbuffer_class import *
import sys
import time
from endprogops import *

myaddressbookholder=addressbookholder()

#-------------------------------------------------------------------------------

bookbuffer=addressbook('testbook1')	

cardcreation=addresscard()
cardcreation.actualcard[0].fieldvalue='Joe'
cardcreation.actualcard[1].fieldvalue='98765432'
cardcreation.createnewfield('Email', 'test@test.com')

bookbuffer.addcard(cardcreation)

cardcreation=addresscard()
cardcreation.actualcard[0].fieldvalue='Mary'
cardcreation.actualcard[1].fieldvalue='9282672652'

bookbuffer.addcard(cardcreation)

cardcreation=addresscard()
cardcreation.actualcard[0].fieldvalue='John'
cardcreation.actualcard[1].fieldvalue='920282672'

bookbuffer.addcard(cardcreation)

myaddressbookholder.createbook(bookbuffer)

#--------------------------------------------------------------------------------------------


bookbuffer=addressbook('testbook2')	

cardcreation=addresscard()
cardcreation.actualcard[0].fieldvalue='Mark'
cardcreation.actualcard[1].fieldvalue='98765432'

bookbuffer.addcard(cardcreation)

cardcreation=addresscard()
cardcreation.actualcard[0].fieldvalue='Henry'
cardcreation.actualcard[1].fieldvalue='98765432'

bookbuffer.addcard(cardcreation)

cardcreation=addresscard()
cardcreation.actualcard[0].fieldvalue='Seville'
cardcreation.actualcard[1].fieldvalue='98765432'

bookbuffer.addcard(cardcreation)

myaddressbookholder.createbook(bookbuffer)

#----------------------------------------------------------------------------------------------

test=myaddressbookholder.endprogops()

#print test