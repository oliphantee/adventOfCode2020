import copy as cp

inputFile=open("ingredientList.txt")

fullDict={}
allIngredients=[]

for line in inputFile:
    ingredientsInALine=line.split("(contains ")[0].split(" ")
    allergensInALine=line.split("(contains ")[1].strip("\n").strip(")")
    for allergen in allergensInALine.split(","):
        key=allergen.strip(" ")
        if key not in fullDict:
            fullDict[key]={}
        for ingredient in ingredientsInALine:
            if ingredient in fullDict[key]:
                fullDict[key][ingredient]+=1
            else:
                fullDict[key][ingredient]=1
    for ingredient in ingredientsInALine:
        if(ingredient!=""):
            allIngredients+=[ingredient]

newDict=cp.deepcopy(fullDict)
for allergen in fullDict:
    newDict[allergen].pop('')
    maxOccurances=0
    for ingredient in fullDict[allergen]:
        if fullDict[allergen][ingredient]>maxOccurances:
            maxOccurances=fullDict[allergen][ingredient]
    for ingredient in fullDict[allergen]:
        if fullDict[allergen][ingredient]<maxOccurances:
            newDict[allergen].pop(ingredient)

endDict=cp.deepcopy(newDict)
progress=1
while progress!=0:
    progress=0
    for allergen in endDict:
        if len(endDict[allergen].keys())==1:
            for key in endDict:
                if key!=allergen:
                    if list(endDict[allergen].keys())[0] in endDict[key]:
                        progress=1
                        endDict[key].pop(list(endDict[allergen].keys())[0])

allAllergens=[]
for i in endDict:
    allAllergens+=[(i,list(endDict[i].keys())[0])]

print(allAllergens)
def getKey(item):
    return item[0]
retString=""
for i in sorted(allAllergens,key=getKey):
    retString+=i[1]+","
print(retString)