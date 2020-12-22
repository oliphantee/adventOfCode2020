howRecent={2:0,15:1,0:2,9:3,1:4}
prevNum=20
numTurns=30000000

for turn in range(5,numTurns-1):
    if prevNum in howRecent:
        newNum=turn-howRecent[prevNum]
        howRecent[prevNum]=turn
    else:
        newNum=0
        howRecent[prevNum]=turn
    prevNum=newNum
print(newNum)