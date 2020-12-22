homeworkFile=open("homework.txt","r")

class Node:
    def __init__(self,expression):
        if(len(expression)==1):
            self.data=expression[0]
            self.left=None
            self.right=None
            return
        if(")" in expression[-1]):
            #print(expression)
            count=expression[-1].count(")")
            i=-2
            while count!=0:
                count-=expression[i].count("(")
                count+=expression[i].count(")")
                i-=1
            if i==-len(expression)-1:
                newExpression=[expression[0][1:]]+expression[1:-1]+[expression[-1].strip("\n")[:-1]]
                self.left=Node(["0"])
                self.data="+"
                self.right=Node(newExpression)
            else:
                self.left=Node(expression[:i])
                self.data=expression[i]
                self.right=Node(expression[i+1:])
        else:
            self.left=Node(expression[:-2])
            self.data=expression[-2]
            self.right=Node([expression[-1]])

    def eval(self):
        if self.data.strip("(").strip(")").isnumeric():
            #if(a==0):
            #    print(int(self.data.strip("\n").strip("(").strip(")")))
            #return self.data.strip("(").strip(")")
            return int(self.data.strip("\n").strip("(").strip(")"))
        else:
            if(self.data=="*"):
                #return "("+self.left.eval()+"*"+self.right.eval()+")"
                return self.left.eval()*self.right.eval()
            elif(self.data=="+"):
                #return "("+self.left.eval()+"+"+self.right.eval()+")"
                return self.left.eval()+self.right.eval()
            elif(self.data=="-"):
                #return "("+self.left.eval()+"-"+self.right.eval()+")"
                return self.left.eval()-self.right.eval()
            elif(self.data=="/"):
                #return "("+self.left.eval()+"/"+self.right.eval()+")"
                return self.left.eval()/self.right.eval()
            else:
                print([self.data])
                print("sthing went wrong")
                return None

acc=0
a=0
for line in homeworkFile:
    expression=line.strip("\n").split(" ")
    node=Node(expression)
    answer=node.eval()
    print(answer)
    a+=1
    acc+=answer

print(acc)