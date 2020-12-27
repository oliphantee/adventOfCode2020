inputFile=open("input.txt")

allRules={}

for line in inputFile:
    bigBag=line.split(" contain ")[0]
    allRules[bigBag]={}
    for subBag in line.split(" contain ")[1].strip(".\n").split(", "):
        subName=""
        value=1
        for word in subBag.split(" "):
            if not word.isnumeric():
                subName+=word+" "
            else:
                value=int(word)
        #print(subName)
        allRules[bigBag][subName.strip(" ")]=value

def contains(bigBag,goalBag):
    if bigBag=="no other bags":
        return False
    if bigBag not in allRules:
        bigBag=bigBag+"s"
    if allRules[bigBag]=="no other bags":
        return False
    elif goalBag in allRules[bigBag] or goalBag+"s" in allRules[bigBag]:
        return True
    else:
        for bag in allRules[bigBag]:
            if contains(bag,goalBag):
                return True
    return False

count=0
for bag in allRules:
    #print(bag)
    if (contains(bag,"shiny gold bag")):
        #print("yes")
        count+=1
print(count)
#print(contains("light red bags","shiny gold bag"))
#print(allRules)

def numInside(bigBag):
    if bigBag=="no other bags":
        return 0
    count=0
    if bigBag not in allRules:
        bigBag+="s"
    for bag in allRules[bigBag]:
        #print(bag,allRules[bigBag][bag])
        count+=numInside(bag)*allRules[bigBag][bag]
    return count+1

print(numInside("shiny gold bags")-1)