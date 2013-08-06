#Script expects an array of 2 columns by however many rows. 
#First column should be x values, second column should be y values

def gradientdescentalgorithm():

	def predictionfunc(thetazero, thetaone, thetatwo, thetathree, x):
		predictionfunc=thetazero + (thetaone*x) + (thetatwo * (x^2)) + (thetathree * (x^3))
		return predictionfunc
	
	def errorfunc(thetazero, thetaone, thetatwo, thetathree, x, y):
		errorfunc=predictfunc(thetazero, thetaone, thetatwo, thetathree, x) - y
		return errorfunc

	# def diffcostfunc(prediction, y, numberoftrials):
	# 	diffcostfunc=(1/numberoftrials)*()

	#Initial Parameters
	dataset=[[1,2,3,4], [2,4,6,8]]
	alpha=0.01
	thetazero=0
	thetaone=0
	thetatwo=0
	thetathree=0
	meanerror=1000
	iterationcounter=0

	if (abs(meanerror) <= 0.01) or (iterationcounter==10000):

		xvalues=dataset[:,1]

		for i in range [0:(len(xvalues))]:
			error=errorfunc(thetazero, thetaone, thetatwo, thetathree, dataset[i, 1], dataset[i,2])
			errorlistzero=[]
			errorlistone=[]
			errorlisttwo=[]
			errorlistthree=[]

			errorzeroholder=float(error)
			errorzeroholder.append(errorlistzero)

			erroroneholder=float(error*dataset[i,1])
			erroroneholder.append(errorlistone)

			errortwoholder=float(error*(dataset[i,1]^2))
			errortwoholder.append(errorlisttwo)

			errorthreeholder=float(error*(dataset[i,1]^3))
			errorthreeholder.append(errorlistthree)

		test=sum(errorlistzero)

		thetazero = thetazero - alpha*(1/(float(len(xvalues))))*sum(errorlistzero)
		thetaone = thetaone - alpha*(1/(len(xvalues)))*sum(errorlistone)
		thetatwo = thetatwo - alpha*(1/(len(xvalues)))*sum(errorlisttwo)
		thetathree = thetathree - alpha*(1/(len(xvalues)))*sum(errorlistthree)

		meanerror=sum(errorlist_zero)/float(len(xvalues))
		iterationcounter += 1
		print iterationcounter

	return [thetazero, thetaone, thetatwo, thetathree]

test=gradientdescentalgorithm()