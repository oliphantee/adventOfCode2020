import copy as cp

inputFile=open("input.txt")

allGroups=[]
oneGroup=set()
for line in inputFile:
    if line=="\n":
        allGroups+=[oneGroup]
        oneGroup=set()
    else:
        for letter in line.strip("\n"):
            oneGroup.add(letter)

allGroups+=[oneGroup]
totCount=0
for group in allGroups:
    totCount+=len(group)
print(totCount)

inputFile=open("input.txt")

allGroupsPartB=[]
oneGroupPartB=set(("a","b","c","d","e","f","g","h","i","j","k","l","m",'n','o','p','q','r','s','t','u','v','w','x','y','z'))
for line in inputFile:
    #print([line])
    if line=="\n":
        allGroupsPartB+=[oneGroupPartB]
        oneGroupPartB=set(("a","b","c","d","e","f","g","h","i","j","k","l","m",'n','o','p','q','r','s','t','u','v','w','x','y','z'))
    else:
        newGroup=cp.deepcopy(oneGroupPartB)
        for i in oneGroupPartB:
            if i not in line and i in newGroup:
                #print(i)
                newGroup.remove(i)
        oneGroupPartB=newGroup

allGroupsPartB+=[oneGroupPartB]
totCountB=0
for group in allGroupsPartB:
    #print(len(group))
    totCountB+=len(group)
print(totCountB)
#print(allGroupsPartB)