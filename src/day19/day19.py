inputFile=open("input.txt")
allRules={}

class Rule:
    def __init__(self,id):
        self.id=id
        self.orList=[]
        self.letter=None

    def __str__(self):
        retStr=str(self.id)+":"
        if self.letter!=None:
            retStr+=" "+self.letter+" "
        else:
            for andList in self.orList:
                for ruleId in andList:
                    retStr+=" " + str(allRules[ruleId].id)
                retStr+=" |"
        return retStr[:-1]

    def define(self,line,allRules):
        if '"' in line:
            self.letter=line.strip('"')[0]
        theOrList=line.split(" | ")
        for i in range(len(theOrList)):
            self.orList+=[[]]
            andList=theOrList[i].split(" ")
            for j in range(len(andList)):
                self.orList[i]+=[[]]
                self.orList[i][j]=andList[j]


    def evaluate(self,posStrings):
        newPosStrings=[]
        if self.letter!=None:
            for bstring in posStrings:
                if len(bstring)>0 and bstring[0]==self.letter:
                    newPosStrings.append(bstring[1:])
        else:
            for andList in self.orList:
                curPosStrings=posStrings
                isTrue=True
                for rule in andList:
                    isTrue,curPosStrings=allRules[rule].evaluate(curPosStrings)
                    if(isTrue==False):
                        break
                if(isTrue==True):
                    newPosStrings+=curPosStrings
        return len(newPosStrings)!=0, newPosStrings

ruleZero=None
count=0

for line in inputFile:
    if(len(line.split(":"))>1):
        id=line.split(":")[0]
        aRule=Rule(id)
        allRules[id]=aRule
        aRule.define(line.split(":")[1].strip("\n").strip(" "),allRules)
        if id=="0":
            ruleZero=aRule
    elif len(line)>1:
        answer=ruleZero.evaluate([line.strip("\n")])
        if(answer[0] and "" in answer[1]):
            count+=1

print(count)