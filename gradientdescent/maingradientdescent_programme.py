from testprogramme import *

indataset=[[1,2,3,4], [14,20,28,38]]
alpha=0.0001
thetazero=float(0)
thetaone=float(0)
thetatwo=float(0)
thetathree=float(0)

results=gradientdescentalgorithm(indataset, alpha, thetazero, thetaone, thetatwo, thetathree)

print results