import copy as cp

inputFile=open("input.txt")

class SeatLayout:
    def __init__(self,inputFile):
        self.allSeats=[]
        row=0
        for line in inputFile:
            self.allSeats+=[[]]
            for char in line.strip("\n"):
                self.allSeats[row]+=[char]
            row+=1
        self.allSeats=[["."]*len(self.allSeats[0])]+self.allSeats+[["."]*len(self.allSeats[0])]
        #print(self.allSeats)
        for i,_ in enumerate(self.allSeats):
            #print(self.allSeats[i])
            self.allSeats[i]=["."]+self.allSeats[i]+["."]
        #print(self.allSeats)

    def print(self):
        for row in range(1,len(self.allSeats)-1):
            print(self.allSeats[row][1:-1])

    def getNeighbors(self,row,col):
        count=0
        for curRow in range(row-1,row+2):
            count+=len(list(filter(lambda x:x=="#",self.allSeats[curRow][col-1:col+2])))
        if self.allSeats[row][col]=="#":
            count-=1
        return count

    def getNumSeen(self,row,col):
        count=0
        vecList=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        for vec in vecList:
            curCol=col+vec[1]
            curRow=row+vec[0]
            while curCol<len(self.allSeats[0]) and curRow<len(self.allSeats) and curCol>=0 and curRow>=0:
                if(self.allSeats[curRow][curCol]=="#"):
                    count+=1
                    break
                if(self.allSeats[curRow][curCol]=="L"):
                    break
                curCol+=vec[1]
                curRow+=vec[0]
        return count

    def printNumSeen(self):
        for row in range(1,len(self.allSeats)-1):
            print("[",end="")
            for col in range(1,len(self.allSeats[row])-1):
                print("'"+str(self.getNumSeen(row,col))+"'",end=", ")
            print("]")



    def printNeighbors(self):
        for row in range(1,len(self.allSeats)-1):
            print("[",end="")
            for col in range(1,len(self.allSeats[row])-1):
                print("'"+str(self.getNeighbors(row,col))+"'",end=", ")
            print("]")

    def timeStep(self):
        allSeatsCopy=cp.deepcopy(self.allSeats)
        for row in range(len(self.allSeats)):
            for col in range(len(self.allSeats[row])):
                #print(row,col,self.getNeighbors(row,col),[self.allSeats[row][col]])
                if self.allSeats[row][col]=="L" and self.getNumSeen(row,col)==0:
                    allSeatsCopy[row][col]="#"
                if self.allSeats[row][col]=="#" and self.getNumSeen(row,col)>=5:
                    allSeatsCopy[row][col]="L"
        #self.printNeighbors()
        self.allSeats=allSeatsCopy
        #self.print()

    def getTotalOccupied(self):
        count=0
        for curRow in range(len(self.allSeats)):
            count+=len(list(filter(lambda x:x=="#",self.allSeats[curRow])))
        return count

seatLayout=SeatLayout(inputFile)
prevAllSeats=None
while(prevAllSeats!=seatLayout.allSeats):
    #seatLayout.printNumSeen()
    #seatLayout.print()
    #print()
    prevAllSeats=cp.deepcopy(seatLayout.allSeats)
    seatLayout.timeStep()
print(seatLayout.getTotalOccupied())