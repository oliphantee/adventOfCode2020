import sys

inputFile=open("input.txt")

def getTimeToWait(busId,curTime):
    arriveTime=0
    while arriveTime<curTime:
        arriveTime+=busId
    busId-curTime%busId
    return arriveTime-curTime

# this code is from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# the rest of the code is writen by me

curTime=int(inputFile.readline())
buses=list(inputFile.readline().split(","))
#print(curTime,buses)
bestWait=sys.maxsize
bestId=0
offset=0
allBuses={}

for bus in buses:
    if bus.isnumeric():
        posTime=getTimeToWait(int(bus),curTime)
        if posTime<bestWait:
            bestWait=posTime
            bestId=int(bus)
        allBuses[offset]=int(bus)
    offset+=1

print(bestId*bestWait) # part 1

print(allBuses.keys(),allBuses.values())
aArray=[]
for i in allBuses:
    aArray+=[allBuses[i]-i]
print(chinese_remainder(allBuses.values(),aArray))