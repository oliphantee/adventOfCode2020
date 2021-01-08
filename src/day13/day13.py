import sys

inputFile=open("input.txt")

def getTimeToWait(busId,curTime):
    arriveTime=0
    while arriveTime<curTime:
        arriveTime+=busId
    busId-curTime%busId
    return arriveTime-curTime

curTime=int(inputFile.readline())
buses=list(inputFile.readline().split(","))
#print(curTime,buses)
bestWait=sys.maxsize
bestId=0
offset=0
allBuses={}

for bus in buses:
    if bus.isnumeric():
        posTime=getTimeToWait(int(bus),curTime)
        if posTime<bestWait:
            bestWait=posTime
            bestId=int(bus)
        allBuses[offset]=int(bus)
    offset+=1

print(bestId*bestWait) # part 1

notDone=True
curGuess=0
print(allBuses)
while notDone:
    curGuess+=allBuses[0]
    works=True
    for offset in allBuses:
        if curGuess%allBuses[offset]-offset!=0:
            works=False
    if works==True:
        notDone=False
    #print(curGuess)

print(curGuess)