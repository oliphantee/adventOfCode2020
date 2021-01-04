import math as mt

inputFile=open("input.txt")

curDirection=[0,1]
curLoc=[0,0]
curAngle=0

for line in inputFile:
    direction=line[0]
    #print(direction,int(line[1:]))
    if direction=="N":
        curLoc[0]+=int(line[1:])
    elif direction=="S":
        curLoc[0]-=int(line[1:])
    elif direction=="E":
        curLoc[1]+=int(line[1:])
    elif direction=="W":
        curLoc[1]-=int(line[1:])
    elif direction=="F":
        curLoc[0]+=curDirection[0]*int(line[1:])
        curLoc[1]+=curDirection[1]*int(line[1:])
    elif direction=="R":
        curAngle-=int(line[1:])/360*2*mt.pi
        curDirection=[mt.sin(curAngle),mt.cos(curAngle)]
    elif direction=="L":
        curAngle+=int(line[1:])/360*2*mt.pi
        curDirection=[mt.sin(curAngle),mt.cos(curAngle)]
    #print(curAngle,curDirection,curLoc)

print(curLoc)
print(abs(curLoc[0])+abs(curLoc[1]))

inputFile=open("input.txt")

curLoc2=[0,0]
wayPoint=[1,10]

for line in inputFile:
    direction=line[0]
    #print(direction,int(line[1:]))
    if direction=="N":
        wayPoint[0]+=int(line[1:])
    elif direction=="S":
        wayPoint[0]-=int(line[1:])
    elif direction=="E":
        wayPoint[1]+=int(line[1:])
    elif direction=="W":
        wayPoint[1]-=int(line[1:])
    elif direction=="F":
        curLoc2[0]+=wayPoint[0]*int(line[1:])
        curLoc2[1]+=wayPoint[1]*int(line[1:])
    elif direction=="R":
        curDist=(wayPoint[0]**2+wayPoint[1]**2)**.5
        curAngle=mt.atan(wayPoint[0]/wayPoint[1])
        if wayPoint[1]<0:
            curAngle+=mt.pi
        curAngle-=int(line[1:])/360*2*mt.pi
        wayPoint=[mt.sin(curAngle)*curDist,mt.cos(curAngle)*curDist]
    elif direction=="L":
        curDist=(wayPoint[0]**2+wayPoint[1]**2)**.5
        curAngle=mt.atan(wayPoint[0]/wayPoint[1])
        if wayPoint[1]<0:
            curAngle+=mt.pi
        curAngle+=int(line[1:])/360*2*mt.pi
        wayPoint=[mt.sin(curAngle)*curDist,mt.cos(curAngle)*curDist]
    #print(wayPoint,curLoc2)

print(curLoc2)
print(abs(curLoc2[0])+abs(curLoc2[1]))