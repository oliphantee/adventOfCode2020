MAXVAL=99999999999999

class CupList:
    def __init__(self):
        self.top=None
        self.length=0
        self.allCups={}

    def addCup(self,value,currentCup):
        if self.top==None:
            self.top=value
            self.allCups[value]=None
        elif(self.length==1):
            self.allCups[value]=currentCup
            self.allCups[currentCup]=value
        else:
            self.allCups[value]=self.allCups[currentCup]
            self.allCups[currentCup]=value
        self.length+=1
        return value

    def drawAfter(self,currentCup):
        retVal=self.allCups[currentCup]
        if(self.length>1):
            if(self.allCups[currentCup]==self.top):
                self.top=self.allCups[self.allCups[currentCup]]
            toRemove=self.allCups[currentCup]
            self.allCups[currentCup]=self.allCups[toRemove]
            self.allCups.pop(toRemove)
        else:
            #this shouldn't be necessary in this case, but it might be for part 2
            self.top=None
            self.bot=None
        self.length-=1
        return retVal

    def printAllCups(self):
        topHasBeenSeen=0
        curCup=self.top
        while topHasBeenSeen!=1:
            print(curCup)
            curCup=self.allCups[curCup]
            if(curCup==self.top):
                topHasBeenSeen+=1

    def getString(self):
        topHasBeenSeen=0
        curCup=self.top
        retString=""
        while topHasBeenSeen<1:
            retString+=str(curCup)+","
            curCup=self.allCups[curCup]
            if(curCup==self.top):
                topHasBeenSeen+=1
        return retString

    def printTwoAfter(self,value):
        print(self.allCups[value],self.allCups[self.allCups[value]])


inputFile=open("input.txt")

curCup=None
lowestCup=MAXVAL
highestCup=0
cupList=CupList()
for line in inputFile:
    for value in line:
        if int(value)<lowestCup:
            lowestCup=int(value)
        if int(value) > highestCup:
            highestCup = int(value)
        curCup=cupList.addCup(int(value),curCup)# curCup will be none the first time, but this shouldn't matter

value=highestCup+1
while value!=1000001:
    if int(value)<lowestCup:
        lowestCup=int(value)
    if int(value) > highestCup:
        highestCup = int(value)
    curCup=cupList.addCup(value,curCup)
    value+=1
#cupList.printAllCups()
#print(cupList.allCups[1000000])

def oneMove(cupList,currentCup):
    pickedUpCups=[]
    pickedUpCups+=[cupList.drawAfter(currentCup)]
    pickedUpCups+=[cupList.drawAfter(currentCup)]
    pickedUpCups+=[cupList.drawAfter(currentCup)]

    neededValue=currentCup-1
    while(neededValue not in cupList.allCups):
        neededValue-=1
        if(neededValue<lowestCup):
            neededValue=highestCup

    destCup=neededValue
    destCup=cupList.addCup(pickedUpCups[0],destCup)
    destCup=cupList.addCup(pickedUpCups[1],destCup)
    cupList.addCup(pickedUpCups[2],destCup)

    newCurrentCup=cupList.allCups[currentCup]

    return newCurrentCup

currentCup=cupList.top

for i in range(10000000):
    #print("move",i+1)
    #print("cups:",cupList.getString())
    #print("current cup:",currentCup)
    #print("")
    currentCup=oneMove(cupList,currentCup)
    if(i%1000000==0):
        print(i)
    if(i>9999998):
        cupList.printTwoAfter(1)


cupList.printTwoAfter(1)
#print(cupList.getString())