import copy as cp

inputFile=open("input.txt")

allTiles={}

origin=(0.0,0.0)

for line in inputFile:
    curLoc=origin
    line=line.strip("\n")
    while(len(line)!=0):
        #print(line)
        if line[0]=="e":
            curLoc=(curLoc[0],curLoc[1]+1)
            line=line[1:]
        elif line[0]=="w":
            curLoc=(curLoc[0],curLoc[1]-1)
            line=line[1:]
        elif line[:2]=="ne":
            curLoc=(curLoc[0]+1,curLoc[1]+1/2)
            line=line[2:]
        elif line[:2]=="nw":
            curLoc=(curLoc[0]+1,curLoc[1]-1/2)
            line=line[2:]
        elif line[:2]=="sw":
            curLoc=(curLoc[0]-1,curLoc[1]-1/2)
            line=line[2:]
        elif line[:2]=="se":
            curLoc=(curLoc[0]-1,curLoc[1]+1/2)
            line=line[2:]
    if curLoc in allTiles:
        if(allTiles[curLoc]=="b"):
            allTiles[curLoc]="w"
        else:
            allTiles[curLoc]="b"
    else:
        allTiles[curLoc]="b"

print(allTiles)
def getCount(allTiles):
    countBlack=0
    countWhite=0
    for i in allTiles:
        if allTiles[i]=="b":
            countBlack+=1
        else:
            countWhite+=1
    return countBlack,countWhite
print(getCount(allTiles))

def morningFlipTiles(allTiles):
    newTiles=cp.deepcopy(allTiles)
    for i in allTiles:
        #print(i)
        #print(neighbors(i))
        countForI=0
        for j in neighbors(i):
            curCount=0
            for k in neighbors(j):
                if k in allTiles and allTiles[k]=="b":
                    curCount+=1
            if j in allTiles and allTiles[j]=="b":
                countForI+=1
                if(curCount==0 or curCount>2):
                    newTiles[j]="w"
            else:
                if(curCount==2):
                    newTiles[j]="b"
        if i in allTiles and allTiles[i] == "b":
            if (countForI == 0 or countForI > 2):
                newTiles[i] = "w"
        else:
            if(countForI==2):
                newTiles[i]="b"
    return newTiles

def neighbors(index):
    allLocs=[]
    allLocs+=[(index[0]-1,index[1]-1/2)]
    allLocs+=[(index[0]+1,index[1]+1/2)]
    allLocs+=[(index[0]+1,index[1]-1/2)]
    allLocs+=[(index[0]-1,index[1]+1/2)]
    allLocs+=[(index[0],index[1]+1)]
    allLocs+=[(index[0],index[1]-1)]
    return allLocs


for i in range(100):
    allTiles=morningFlipTiles(allTiles)
    if i>80:
        print(i+1,getCount(allTiles))
