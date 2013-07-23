from addresscard_class import *

TestingName='Joe'
TestingNumber= '983728291'
mycard=addresscard(TestingName, TestingNumber)

mycard.display()

mycard.createnewfield('Address', 'I wish I had an address to put here')

mycard.display()