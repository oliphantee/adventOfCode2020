passwdListFile=open("passwordList.txt","r")
passwdList=[]

totCount=0

for i in passwdListFile:
    line=i.split()
    bounds=line[0].split("-")
    minBound=int(bounds[0])
    maxBound=int(bounds[1])
    passwd=line[2]
    letter=line[1][0]
    #numOccurance=passwd.count(letter)
    #print(passwd.count(letter))
    #print("letter: "+letter+", count: "+str(numOccurance)+", min: "+str(minBound)+" , max:"+str(maxBound)+", password: "+passwd)
    #if(numOccurance>=minBound and numOccurance<=maxBound):
    #    totCount+=1
    #else:
    #    print(line)
    curCount=0
    if(minBound<=len(passwd) and passwd[minBound-1]==letter):
        curCount+=1
    if(maxBound<=len(passwd) and passwd[maxBound-1]==letter):
        curCount+=1
    if(curCount==1):
        totCount+=1

print(totCount)