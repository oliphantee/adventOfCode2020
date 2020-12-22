inputFile=open("input.txt")
allRules=[]

import copy as cp

class Rule:
    def __init__(self,id):
        self.id=id
        self.orList=[]
        self.letter=None

    def define(self,line,allRules):
        if line.strip('"').isalpha():
            self.letter=line.strip('"')[0]
        theOrList=line.split("|")
        for i in range(len(theOrList)):
            self.orList+=[[]]
            andList=theOrList[i].split(" ")
            for j in range(len(andList)):
                self.orList[i]+=[[]]
                isFilled=False
                for rule in allRules:
                    if rule.id==andList[j]:
                        self.orList[i][j]=rule
                        isFilled=True
                if(isFilled==False):
                    self.orList[i][j]=Rule(andList[j])

    def evaluate(self,aString):
        # print(self.id,aString)
        # print(self.orList)
        # print(self.letter)
        bstring=cp.deepcopy(aString)
        if self.letter!=None:
            if bstring[0]==self.letter:
                return True, bstring[1:]
            else:
                return False, bstring[1:]
        isOr=False
        for ruleSet in self.orList:
            isTrue=True
            for rule in ruleSet:
                isTrue,bstring=rule.evaluate(bstring)
                if(isTrue==False):
                    break
            if(isTrue==False):
                bstring=cp.deepcopy(aString)
            if(isTrue==True):
                isOr=True
                break
        return isOr, bstring

ruleZero=None
count=0

for line in inputFile:
    if(len(line.split(":"))>1):
        id=line.split(":")[0]
        aRule=Rule(id)
        allRules+=[aRule]
        aRule.define(line.split(":")[1].strip("\n").strip(" "),allRules)
        # if id=="65":
        #     print(line.split(":")[1].strip("\n").strip(" "))
        if id=="0":
            ruleZero=aRule
    else:
        if(count!=0):
            print(ruleZero.evaluate(line.strip("\n")))
        count=1

print(ruleZero.evaluate("b"))