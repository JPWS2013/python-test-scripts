import numpy as np

def gradientdescentalgorithm(indataset, alpha, thetazero, thetaone, thetatwo, thetathree):
	#Initial Parameters
	#indataset=[[1,2,3,4], [2,4,6,8]]
	dataset=np.array(indataset)
	# alpha=0.0001
	# thetazero=float(0)
	# thetaone=float(0)
	# thetatwo=float(0)
	# thetathree=float(0)
	thetazero=float(thetazero)
	thetaone=float(thetaone)
	thetatwo=float(thetatwo)
	thetathree=float(thetathree)
	meanerror=1000
	meanerror2=1000
	iterationcounter=0

	xvalues=dataset[0, :]

	meanerrorcollection={}

	while (abs(meanerror) >= 0.00000001) or (abs(meanerror2) >= 0.00000001) or (abs(meanerror3) >= 0.00000001) or (abs(meanerror4) >= 0.00000001): # and (iterationcounter<2000000):
		errorlistzero=[]
		errorlistone=[]
		errorlisttwo=[]
		errorlistthree=[]

		xvalues=dataset[0,:]

		for i in range (len(xvalues)):


			inputvariable=float(dataset[0,i])
			outputvariable=float(dataset[1,i])
			
			prediction= thetazero + (thetaone*inputvariable) + (thetatwo * inputvariable*inputvariable) + (thetathree * inputvariable * inputvariable * inputvariable)
			error=prediction - (outputvariable)


			errorzeroholder=error
			errorlistzero.append(errorzeroholder)

			erroroneholder=error*inputvariable
			errorlistone.append(erroroneholder)

			errortwoholder=error*(inputvariable*inputvariable)
			errorlisttwo.append(errortwoholder)

			errorthreeholder=error*(inputvariable*inputvariable*inputvariable)
			errorlistthree.append(errorthreeholder)

		thetazero = thetazero - alpha*(1/(float(len(xvalues))))*sum(errorlistzero)
		thetaone = thetaone - alpha*(1/(float(len(xvalues))))*sum(errorlistone)
		thetatwo = thetatwo - alpha*(1/(float(len(xvalues))))*sum(errorlisttwo)
		thetathree = thetathree - alpha*(1/(float(len(xvalues))))*sum(errorlistthree)

		meanerror=sum(errorlistzero)/float(len(xvalues))
		meanerror2=sum(errorlistone)/float(len(xvalues))
		meanerror3=sum(errorlisttwo)/float(len(xvalues))
		meanerror4=sum(errorlistthree)/float(len(xvalues))

		meanerrorcollection[meanerror]=[thetazero, thetaone, thetatwo, thetathree]
		iterationcounter += 1


	return [thetazero, thetaone, thetatwo, thetathree]


	# if (abs(meanerror) <= 0.00000001) or (abs(meanerror2) <= 0.00000001):

	# 	print "I'm Perfect!"
	# 	return [thetazero, thetaone, thetatwo, thetathree]

	# else:

	# 	listoferrors=meanerrorcollection.keys()
	# 	listoferrors.sort()
	# 	keytoanswer=listoferrors[0]
	# 	answer=meanerrorcollection[keytoanswer]
	# 	return answer