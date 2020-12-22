inputFile=open("testCase.txt")
import copy as cp


class grid:
    def __init__(self,initialState):
        self.matrix=[]
        for x in range(23):
            self.matrix+=[[]]
            for y in range(23):
                self.matrix[x]+=[[]]
                for z in range(15):
                    self.matrix[x][y]+=["."]
        z=7
        for x in range(7,len(initialState)+7):
            for y in range(7,len(initialState[x-7])+7):
                if initialState[x-7][y-7]=="#":
                    self.matrix[x][y][z]=initialState[x-7][y-7]

    def fillSides(self):
        if "#" in self.matrix[0]:
            for y in range(len(self.matrix[0])):
                for z in range(len(self.matrix[0][y])):
                    self.matrix[:][y][z]=["."]+self.matrix[:][y][z]

        if "#" in self.matrix[-1]:
            for y in range(len(self.matrix[-1])):
                for z in range(len(self.matrix[-1][y])):
                    self.matrix[:][y][z]=self.matrix[:][y][z]+["."]

        if "#" in self.matrix[:][0]:
            for x in range(len(self.matrix)):
                for z in range(len(self.matrix[x][0])):
                    self.matrix[x][:][z]=["."]+self.matrix[x][:][z]

        if "#" in self.matrix[:][-1]:
            for x in range(len(self.matrix)):
                for z in range(len(self.matrix[x][-1])):
                    self.matrix[x][:][z]=self.matrix[x][:][z]+["."]

        if "#" in self.matrix[:][:][0]:
            for x in range(len(self.matrix)):
                for y in range(len(self.matrix[x])):
                    self.matrix[x][y][:]=["."]+self.matrix[x][y][:]

        if "#" in self.matrix[-1]:
            for x in range(len(self.matrix)):
                for y in range(len(self.matrix[x])):
                    self.matrix[x][y][:]=self.matrix[x][y][:]+["."]

    def getNeighbors(self,x,y,z):
        retList=[]
        retList+=[self.matrix[x][y][z+1]]
        retList+=[self.matrix[x][y][z-1]]
        retList+=[self.matrix[x][y+1][z]]
        retList+=[self.matrix[x][y-1][z]]
        retList+=[self.matrix[x+1][y][z]]
        retList+=[self.matrix[x-1][y][z]]
        retList+=[self.matrix[x+1][y+1][z]]
        retList+=[self.matrix[x-1][y+1][z]]
        retList+=[self.matrix[x+1][y-1][z]]
        retList+=[self.matrix[x+1][y+1][z+1]]
        retList+=[self.matrix[x-1][y+1][z+1]]
        retList+=[self.matrix[x+1][y-1][z+1]]
        retList+=[self.matrix[x+1][y+1][z-1]]
        retList+=[self.matrix[x-1][y+1][z-1]]
        retList+=[self.matrix[x+1][y-1][z-1]]
        retList+=[self.matrix[x][y+1][z+1]]
        retList+=[self.matrix[x][y+1][z+1]]
        retList+=[self.matrix[x][y-1][z+1]]
        retList+=[self.matrix[x][y+1][z-1]]
        retList+=[self.matrix[x][y+1][z-1]]
        retList+=[self.matrix[x][y-1][z-1]]
        retList+=[self.matrix[x+1][y][z+1]]
        retList+=[self.matrix[x-1][y][z+1]]
        retList+=[self.matrix[x+1][y][z+1]]
        retList+=[self.matrix[x+1][y][z-1]]
        retList+=[self.matrix[x-1][y][z-1]]
        retList+=[self.matrix[x+1][y][z-1]]
        return retList

    def getScore(self,x,y,z):
        neighbors=self.getNeighbors(x,y,z)
        count=0
        for i in neighbors:
            if i=="#":
                count+=1
        return count

    def getTotAlive(self):
        count=0
        for x in self.matrix:
            for y in x:
                for z in y:
                    if z=="#":
                        count+=1
        return count

    def newStep(self):
        self.fillSides()
        newMatrix=cp.deepcopy(self.matrix)
        for x in range(1,len(self.matrix)-1):
            for y in range(1,len(self.matrix[x])-1):
                for z in range(1,len(self.matrix[x][y])-1):
                    score=self.getScore(x,y,z)
                    if score==3:
                        newMatrix[x][y][z]="#"
                    elif score==2 and self.matrix[x][y][z]=="#":
                        newMatrix[x][y][z]="#"
                    else:
                        newMatrix[x][y][z]="."
        self.matrix=newMatrix

    def print(self):
        for x in range(len(self.matrix)):
            #if "#" in self.matrix[x][:][:]:
                for y in range(len(self.matrix[x])):
                    for z in range(len(self.matrix[x][y])):
                        print(self.matrix[x][y][z],end=",")
                    print("")
                print("")

inputText=[]
for line in inputFile:
    inputText+=[line]

myGrid=grid(inputText)
print(myGrid.getTotAlive())
myGrid.print()
myGrid.newStep()
myGrid.print()
myGrid.newStep()
#myGrid.newStep()
#myGrid.newStep()
#myGrid.newStep()
#myGrid.newStep()
print(myGrid.getTotAlive())
#myGrid.print()