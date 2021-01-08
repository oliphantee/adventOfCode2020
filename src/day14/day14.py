import copy as cp

inputFile=open("input.txt")

def applyMask(value,mask):
    retVal=0
    for i in range(len(mask)):
        if ((value%(2**(i+1))//2**i)==1 and mask[-i-1]!="0") or mask[-i-1]=="1":
            #print(i)
            retVal+=2**i
    return retVal

def applyMask2(memAddress,mask): # part 2 equivalent of applyMask
    retList=[0]
    for i in range(len(mask)):
        #print(retList)
        curVal=(memAddress%(2**(i+1))//2**i)
        if mask[-i-1]!="X":
            if mask[-i-1]=="1":
                curVal=1
            if curVal==1: # if curVal is 0, then nothing needs to be done
                for address in range(len(retList)):
                    retList[address]=retList[address]+2**i
        else:
            copyList=cp.deepcopy(retList)
            for j in range(len(retList)):
                copyList+=[retList[j]+2**i]
            retList=copyList
    return retList

curMask=""
memMap={}
memMap2={}

for line in inputFile:
    if "mask" in line:
        curMask=line.split(" = ")[1].strip("\n")
        #print(curMask)
    else:
        memCommand=line.split("] = ")
        value=int(memCommand[1].strip("\n"))
        memAddress=int(memCommand[0].strip("mem["))
        memMap[memAddress]=applyMask(value,curMask)
        addresses=applyMask2(memAddress,curMask)
        #print(addresses)
        for address in addresses:
            #print(address)
            memMap2[address]=value
        #print(value, memAddress, curMask, memMap[memAddress])

total=0
for i in memMap:
    total+=memMap[i]

print(total) # part 1 answer
total2=0
for i in memMap2:
    total2+=memMap2[i]

print(total2) # part 2 answer