mapFile=open("map.txt","r")
mapList=[]

for line in mapFile:
    newLine=[]
    for char in line:
        if char=='.':
            newLine+=[0]
        elif char=='#':
            newLine+=[1]
    mapList+=[newLine]

allHits=[]

addx=[1,1,1,1,2]
addy=[1,3,5,7,1]
for i in range(len(addx)):
    curLoc=[0,0]
    hits=0
    while curLoc[0]<len(mapList):
        print(curLoc)
        print(mapList[curLoc[0]][curLoc[1]])
        if(mapList[curLoc[0]][curLoc[1]]==1):
            hits+=1
        curLoc[0]=curLoc[0]+addx[i]
        curLoc[1]=(curLoc[1]+addy[i])%len(mapList[0])
    allHits+=[hits]

tot=1
print(allHits)
for i in allHits:
    tot*=i
print(tot)