inputFile=open("input.txt")
import copy as cp


class grid:
    def __init__(self,initialState): # for part 1, just remove all of the 4d portions of the code
        self.blackSet=set()
        z=0
        a=0 # I'm not sure what to use as the 4th dimension, so lets start at the beginning of the alphabet
        for x in range(0,len(initialState)):
            for y in range(0,len(initialState[x])):
                if initialState[x][y]=="#":
                    self.blackSet.add((x,y,z,a))

    def printGrid(self):
        for a in range(-3,3):
            for z in range(-3,3):
                for y in range(-3,8):
                    for x in range(-3,8):
                        if (x,y,z,a) in self.blackSet:
                            print("#",end="")
                        else:
                            print(".", end="")
                    print()
                print()
            print()

    def getNeighbors(self,x,y,z,a):
        retSet=set()
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                for k in range(z-1,z+2):
                    for l in range(a-1,a+2):
                        retSet.add((i,j,k,l))
        retSet.remove((x,y,z,a))
        return retSet

    def getScore(self,x,y,z,a):
        neighbors=self.getNeighbors(x,y,z,a)
        count=0
        for i in neighbors:
            if i in self.blackSet:
                count+=1
        return count

    def getTotAlive(self):
        return len(self.blackSet)

    def newStep(self):
        newBlackSet=cp.deepcopy(self.blackSet)
        setToCheck=set()
        for loc in self.blackSet:
            if loc not in setToCheck:
                setToCheck.add(loc)
            for neighbor in self.getNeighbors(loc[0],loc[1],loc[2],loc[3]):
                if neighbor not in setToCheck:
                    setToCheck.add(neighbor)
        for loc in setToCheck:
            score=self.getScore(loc[0],loc[1],loc[2],loc[3])
            if loc in self.blackSet and score!=2 and score!=3:
                newBlackSet.remove(loc)
            elif loc not in self.blackSet and score==3:
                newBlackSet.add(loc)
        self.blackSet=newBlackSet

inputText=[]
for line in inputFile:
    inputText+=[line]

myGrid=grid(inputText)
print(myGrid.getTotAlive())
myGrid.printGrid()
myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.printGrid()
myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.printGrid()
myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.printGrid()
myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.printGrid()
myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.printGrid()
myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.printGrid()