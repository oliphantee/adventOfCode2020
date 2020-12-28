import copy as cp

inputFile=open("input.txt")

allJolts=[]
for line in inputFile:
    allJolts+=[int(line)]

#print(allJolts)

changeList=[]

curJolt=min(allJolts)
allJolts2=cp.deepcopy(allJolts)
allJolts.remove(curJolt)
while len(allJolts)>=1:
    changeList+=[min(allJolts)-curJolt]
    curJolt=min(allJolts)
    allJolts.remove(curJolt)

#print(changeList)

list1s=filter(lambda x:x==1,changeList)
list3s=filter(lambda x:x==3,changeList)
print((sum(list1s)+1)*(sum(list3s)/3+1)) # part 1 answer

possiblePaths={0:1}
for num in sorted(allJolts2):
    curPosPaths=0
    for i in range(num-3,num):
        if i in possiblePaths:
            curPosPaths+=possiblePaths[i]
    possiblePaths[num]=curPosPaths
#print(sorted(allJolts2))
print(possiblePaths[sorted(allJolts2)[-1]]) # part 2 answer