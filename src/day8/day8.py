inputFile=open("input.txt")

allOperations={}

lineNum=0
for line in inputFile:
    operation,value=line.split(" ")
    allOperations[lineNum]=(operation,int(value),0)
    lineNum+=1

#print(len(allOperations))

def getAccumulator(allOperations):
    done = False
    accumulator = 0
    curOpNum = 0
    while (not done and curOpNum < len(allOperations)):
        if curOpNum not in allOperations:
            print("a")
            break
        else:
            operation, value, numOccurances = allOperations[curOpNum]
            allOperations[curOpNum] = (operation, value, numOccurances + 1)
            if numOccurances == 1:
                done = True
            elif operation == "jmp":
                curOpNum += value - 1
            elif operation == "acc":
                accumulator += value
        curOpNum += 1
    for i in allOperations:
        operation,value,numOccurances=allOperations[i]
        allOperations[i]=(operation,value,0)
    return accumulator,done
print(getAccumulator(allOperations)) # part 1 answer

for i in allOperations:
    operation, value, numOccurances = allOperations[i]
    tryThis=False
    if operation=="nop":
        allOperations[i]="jmp", value, numOccurances
        tryThis=True
    elif operation=="jmp":
        allOperations[i]="nop", value, numOccurances
        tryThis=True
    if(tryThis):
        acc,done=getAccumulator(allOperations)
        if(not done):
            print(i,acc) # part 2 answer
            break
    allOperations[i]=operation, value, numOccurances