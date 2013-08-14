import os

directory='addbookworkfiles'
filelist=os.listdir(directory)

for bookFile in filelist:
	print bookFile
	os.remove(directory + "/" + bookFile)