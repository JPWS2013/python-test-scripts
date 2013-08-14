from addresscard_class import *
from addressbookholder_class import *
from bookbuffer_class import *
import sys
import time


myaddressbookholder=addressbookholder()

myaddressbookholder.openprogops()

allkeys=myaddressbookholder.library.keys()

for eachKey in allkeys:
	print eachKey
	print eachKey=='testbook1'
	print type(eachKey)
	print type('testbook1')