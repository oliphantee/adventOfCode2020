numListFile=open("numList.txt","r")
numList=[]

for i in numListFile:
    numList+=[int(i)]

for i in range(len(numList)):
    for j in range(i+1,len(numList)):
        for k in range(j+1,len(numList)):
            if numList[i]+numList[j]+numList[k]==2020:
                print(numList[i]*numList[j]*numList[k])