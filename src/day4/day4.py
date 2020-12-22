import re

inputFile=open("allPassports.txt")

count=0
bcount=0
eyeColors=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
curPass={}

for line in inputFile:
    if line=="\n":
        bcount+=1
        isTrue=True
        if(len(curPass.keys())==8 or (len(curPass.keys())==7 and "cid" not in curPass.keys())):
            if not(1920<=int(curPass["byr"])<=2002 and 2010<=int(curPass["iyr"])<=2020 and 2020<=int(curPass["eyr"])<=2030 and len(curPass["pid"])==9 and curPass["pid"].isnumeric()):
                isTrue=False
            if curPass["ecl"] not in eyeColors:
                isTrue=False
            if not (curPass["hcl"][0]=="#" and len(curPass["hcl"])==7):
                isTrue=False
            else:
                for i in curPass["hcl"][1:]:
                    if i not in "0123456789abcdef":
                        isTrue=False
            unit=curPass["hgt"][-2:]
            if(unit=="cm"):
                if not 150<=int(curPass["hgt"][:-2])<=193:
                    isTrue=False
            elif(unit=="in"):
                if not 59<=int(curPass["hgt"][:-2])<=76:
                    isTrue=False
            else:
                isTrue=False
            if(isTrue):
                count+=1
        curPass={}
    else:
        for pair in line.split():
            key,value = pair.split(":")
            curPass[key]=value

isTrue=True
if(len(curPass.keys())==8 or (len(curPass.keys())==7 and "cid" not in curPass.keys())):
    bcount+=1
    if not(1920<=int(curPass["byr"])<=2002 and 2010<=int(curPass["iyr"])<=2020 and 2020<=int(curPass["eyr"]<=2030 and len(curPass["pid"]) and curPass["pid"].isnumeric())):
        isTrue=False
    if curPass["ecl"] not in eyeColors:
        isTrue=False
    if not (curPass["hcl"][0]=="#" and len(curPass["hcl"])==7):
        isTrue=False
    else:
        for i in curPass["hcl"][1:]:
            if i not in "0123456789abcdef":
                isTrue=False
    unit=curPass["hgt"][-2:]
    if(unit=="cm"):
        if not 150<=int(curPass["hgt"][:-2])<=193:
            isTrue=False
    elif(unit=="in"):
        if not 59<=curPass["hgt"][:-2]<=76:
            isTrue=False
    else:
        isTrue=False
    if(isTrue):
        count+=1
print(count)