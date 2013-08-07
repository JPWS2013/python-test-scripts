from testprogramme import *
from datetime import datetime
import pandas as pd

dataset=pd.read_csv('out.csv')

#xvalues=dataset['XValues']

#yvalues=dataset['YValues']

starttime=datetime.now()

#indataset=[[1,2,3,4], [50, 130, 280, 500]]#[14,20,28,38]] #x^2 + 3x + 10
alpha=0.00000000000001
thetazero=float(0)
thetaone=float(0)
thetatwo=float(0)
thetathree=float(0)

results=gradientdescentalgorithm(dataset, alpha, thetazero, thetaone, thetatwo, thetathree)

endtime=datetime.now()

print results[0]
print endtime-starttime
print results[1]