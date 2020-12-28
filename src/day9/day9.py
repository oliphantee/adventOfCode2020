inputFile=open("input.txt")

prevNums=[]
lengthPreamble=25
allNums=[]
count=0

def getAllSums(prevNums):
    allSums=[]
    for i in range(len(prevNums)):
        for j in prevNums[:i]+prevNums[i+1:]:
            allSums+=[prevNums[i]+j]
    return allSums

for line in inputFile:
    num=int(line)
    if count<lengthPreamble:
        prevNums+=[num]
    else:
        if num not in getAllSums(prevNums):
            print(num)
            invalidNum=num
            break
        prevNums[count%lengthPreamble]=num
    count+=1
    allNums+=[num]

for i in range(len(allNums)):
    curSumList=[]
    for j in range(i,len(allNums)):
        curSumList+=[allNums[j]]
        if sum(curSumList)==invalidNum:
            print(curSumList)
            #print(min(curSumList)*max(curSumList))
            break
    if sum(curSumList)==invalidNum:
        break

minimum=100000000000000000
maximum=0
for i in curSumList:
    if i<minimum:
        minimum=i
    if i>maximum:
        maximum=i
print(maximum+minimum)
print(min(curSumList))
print(max(curSumList))