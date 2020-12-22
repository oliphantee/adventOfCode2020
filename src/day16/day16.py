rulesFile=open("rules.txt","r")
ticketsFile=open("allTickets.txt","r")
allPossible=[]
maybePossible=[]
allValid=[]
k=0

for i in rulesFile:
    ranges=i.split(":")[1].split("or")
    low=int(ranges[0].split('-')[0])
    high=int(ranges[0].split('-')[1])
    allPossible+=[[]]
    for j in range(low,high+1):
        allPossible[k]+=[j]

    low=int(ranges[1].split('-')[0])
    high=int(ranges[1].split('-')[1])

    for j in range(low,high+1):
        allPossible[k]+=[j]
    k+=1


totWrong=0
maybePossible=[]

for i in range(20):
    line=[]
    for j in range(20):
        line+=[1]
    maybePossible+=[line]

count=0


for line in ticketsFile:
    nums=line.split(",")
    actWrong=1
    for num in range(len(nums)):
        wrong=0
        for adict in range(len(allPossible)):
            if int(nums[num]) in allPossible[adict]:
                wrong=1
        if wrong==0:
            actWrong=0
            totWrong+=int(nums[num])
    if actWrong == 1:
        for num in range(len(nums)):
            for bdict in range(20):
                if int(nums[num]) not in allPossible[bdict]:
                    maybePossible[num][bdict]=0

for i in maybePossible:
    print(i)

for i in range(20):
    for j in range(len(maybePossible)):
        if sum(maybePossible[j])==1:
            for k in range(len(maybePossible[j])):
                if maybePossible[j][k]==1:
                    for l in range(len(maybePossible)):
                        maybePossible[l][k]=0
    for i in maybePossible:
        print(i)
print(totWrong)

for i in maybePossible:
    print(i)