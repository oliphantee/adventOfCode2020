inputFile=open("input.txt")

def getRowCol(seatString):
    row=0
    col=0
    rowStep=64
    colStep=4
    for char in seatString:
        if char=="F":
            rowStep/=2
        if char=="B":
            row+=rowStep
            rowStep/=2
        if char=="R":
            col+=colStep
            colStep/=2
        if char=="L":
            colStep/=2
    return row,col

def getSeatId(row,col):
    return row*8+col

allIds=set()
for line in inputFile:
    row,col=getRowCol(line.strip("\n"))
    #print(row,col)
    allIds.add(getSeatId(row,col))

print(max(allIds))
#print(allIds)
i=0
done=False
while(not done):
    if i not in allIds and i+1 in allIds and i-1 in allIds:
        done=True
    i+=1
print(i)