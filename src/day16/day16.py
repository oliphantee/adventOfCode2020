inputFile=open("input.txt","r")
allPossible=[]
maybePossible=[]
allValid=[]
k=0
totWrong=0
myTicket=[]

for line in inputFile:
    if "or" in line: # this means it is a rule
        ranges=line.split(":")[1].split("or")
        low=int(ranges[0].split('-')[0])
        high=int(ranges[0].split('-')[1])
        allPossible+=[[]]
        for j in range(low,high+1):
            allPossible[k]+=[j]

        low=int(ranges[1].split('-')[0])
        high=int(ranges[1].split('-')[1])

        for j in range(low,high+1):
            allPossible[k]+=[j]
        maybePossible+=[[]]
        for i in range(k):
            maybePossible[k]+=[1]
        for i in range(len(maybePossible)):
            maybePossible[i]+=[1]
        k+=1

    elif "," in line: # this means it is a ticket, will include my ticket
        nums=line.split(",")
        if(myTicket==[]):
            myTicket=nums
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

print(totWrong)
# for i in maybePossible:
#     print(i)

for _ in range(len(maybePossible)-1): # this should be the number of iterations necessary
    for i in range(len(maybePossible)):
        if sum(maybePossible[i])==1:
            index=0
            for j in range(len(maybePossible[i])):
                if maybePossible[i][j]==1:
                    for k in range(len(maybePossible)):
                        if k!=i:
                            maybePossible[k][j]=0

#print(maybePossible)
tot=1
for j in range(len(maybePossible)):
    for i in range(6):
        if maybePossible[j][i]==1:
            #print(int(myTicket[j]))
            tot*=int(myTicket[j])

print(tot) # part 2 answer