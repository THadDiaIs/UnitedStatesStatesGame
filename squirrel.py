import pandas as pd

analysis = {'Gray':0,'Red':0,'Black':0,'White':0,'Cinnamon':0}

with open('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv') as SqData:
	pSData=pd.read_csv(SqData)

for k in analysis:
	analysis[k] = len(pSData[pSData['Highlight Fur Color'] == k])

#tmp1 = pSData['Highlight Fur Color'].to_dict()
#tmp1 = pd.DataFrame(pSData['Gray' in pSData['Highlight Fur Color']])
#print(tmp1)
#print(tmp0)
#print(pSData)

#for k in tmp1:
#	if type(tmp1[k]) != float:
#		for i in tmp1[k].strip(',').split():
#			print(i)

newAnalysis = pd.DataFrame({'Colors':analysis.keys(),'Counts':analysis.values()})
newAnalysis.to_csv('squirrelCount.csv')
print(newAnalysis)