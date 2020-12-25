cardPublicKey=8458505
doorPublicKey=16050997

DIVNUM=20201227
origSubjNum=7 #? this isn't super clear


def transform(subjectNum,loopSize):
    value=1
    for i in range(loopSize):
        value*=subjectNum
        value=value%DIVNUM
    #print(value)
    return value

def transformOnce(subjectNum,value):
    value*=subjectNum
    value=value%DIVNUM
    return value

cardLoopNum=0
value=1
while(value!=cardPublicKey):
    #print(value)
    cardLoopNum+=1
    value=transformOnce(origSubjNum,value)

doorLoopNum=0
value=1
while(value!=doorPublicKey):
    #print(value)
    doorLoopNum+=1
    value=transformOnce(origSubjNum,value)

print(cardLoopNum,doorLoopNum)
print(transform(doorPublicKey,cardLoopNum))
print(transform(cardPublicKey,doorLoopNum))