homeworkFile=open("homework.txt","r")

# I looked at https://www.tutorialspoint.com/Convert-Infix-to-Postfix-Expression for part 2 and modified it to suit the problem

def preced(ch):
    if ch=="+" or ch=="-":
        return 2
    elif ch=="/" or ch=="x" or ch=="*": # for part 1, modify this to return 2
        return 1
    else:
        return 0

def inToPost(infix):
    stk=[]
    stk.append("#")
    postFix=[]
    for ch in infix:
        if ch.isnumeric():
            postFix+=[ch]
        elif ch=="(":
            stk.append(ch)
        elif ch==")":
            while(stk[-1]!="#" and stk[-1]!="("):
                newCh=stk.pop(-1)
                #print("a",newCh)
                postFix+=[newCh]
            stk.pop()
        else:
            if preced(ch)>preced(stk[-1]):
                stk.append(ch)
            else:
                while(stk[-1]!="#" and preced(ch)<=preced(stk[-1])):
                    newCh=stk.pop(-1)
                    postFix+=[newCh]
                stk.append(ch)
    while len(stk)>1:
        newCh=stk.pop(-1)
        #print("C",newCh)
        postFix+=[newCh]
    return postFix

def evalPost(postFix):
    stk=[]
    for char in postFix:
        if char.isnumeric():
            stk.append(char)
        else:
            oper1=stk.pop(-1)
            oper2=stk.pop(-1)
            if char=="+":
                stk.append(int(oper1)+int(oper2))
            elif char=="*":
                stk.append(int(oper1)*int(oper2))
    return stk[0]

acc=0
for line in homeworkFile:
    expression=line.strip("\n")
    expression=inToPost(expression.replace(" ",""))
    answer=evalPost(expression)
    acc+=answer

print(acc)