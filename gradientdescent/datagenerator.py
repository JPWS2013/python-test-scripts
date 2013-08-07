import numpy as np
from pandas import DataFrame
import pandas as pd

listofnumbers=range(0, 1001, 1)

#datadictionary={'XValues': listofnumbers}

randomnumberlist=np.random.normal(size=(1,1001))

indexcounter=0
finalresultlist=[]

for eachNumber in listofnumbers:
	x=eachNumber
	exactresult=(35*x*x)-(25*x*x)+40
	finalresult=exactresult + randomnumberlist[0, indexcounter]
	finalresultlist.append(finalresult)
	indexcounter += 1

datadictionary={'XValues': listofnumbers, 'YValues': finalresultlist}

finaldata=DataFrame(datadictionary)

finaldata.to_csv('out.csv')