inputFile=open("input.txt")
allTiles=[]
idList=[]
idDict={}

curTile=[]
for line in inputFile:
    if "Tile" in line:
        if curTile!=[]:
            allTiles+=[curTile]
        idList+=[line.strip("\n").split(" ")[1].strip(":")]
        curTile=[]
        j=0
    elif len(line)>2:
        curTile+=[[]]
        for i in line.strip("\n"):
            curTile[j]+=[i]
        j+=1
allTiles+=[curTile]

def getEdges(tile):
    #print(tile)
    topEdge=tile[0]
    botEdge=tile[-1]
    leftEdge=[]
    rightEdge=[]
    for line in tile:
        #print(line)
        leftEdge+=[line[0]]
        rightEdge+=[line[-1]]
    return [topEdge,botEdge,leftEdge,rightEdge]
print(len(allTiles))
allEdges={}
for tile in allTiles:
    for edge in getEdges(tile):
        if str(edge) not in allEdges and str(edge[-1::-1]) not in allEdges:
            #print(edge)
            allEdges[str(edge)]=1
        else:
            #print("a",edge)
            if str(edge) in allEdges:
                #print("b")
                #print("a")
                allEdges[str(edge)]+=1
            else:
                #print("a")
                allEdges[str(edge[-1::-1])]+=1
print(len(allEdges))

for tile in range(len(allTiles)):
    for edge in getEdges(allTiles[tile]):
        if (str(edge) in allEdges and allEdges[str(edge)]==1) or (str(edge[-1::-1]) in allEdges and allEdges[str(edge[-1::-1])]==1):
            if idList[tile] not in idDict:
                idDict[idList[tile]]=1
            else:
                idDict[idList[tile]]+=1
print(idDict)

cornerList=[]
for i in range(len(idDict.values())):
    if list(idDict.values())[i]==2:
        cornerList+=[list(idDict.keys())[i]]
print(cornerList)

product=1
for i in cornerList:
    product*=int(i)

print(product)
