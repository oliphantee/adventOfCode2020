import copy as cp

decksFile=open("decks.txt")

class Card:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value

class Deck:
    def __init__(self):
        self.top=None
        self.bot=None
        self.length=0

    def copy(self,newLen):
        newDeck=Deck()
        allCards=[]
        while(self.length!=0):
            allCards+=[self.drawCard()]
        for card in allCards:
            self.addCard(card)
            if newDeck.length<newLen:
                newDeck.addCard(card)
        return newDeck

    def addCard(self,value):
        newCard=Card(value)
        if self.top==None:
            self.top=newCard
            self.bot=newCard
            newCard.next=None
            newCard.next=None
        else:
            self.bot.next=newCard
            newCard.prev=self.bot
            self.bot=newCard
            newCard.next=None
        self.length+=1

    def drawCard(self):
        retVal=self.top.value
        if(self.length>1):
            self.top.next.prev=None
            self.top=self.top.next
        else:
            self.top=None
        self.length-=1
        return retVal

    def printAllCards(self):
        curCard=self.top
        while curCard!=None:
            print(curCard.value)
            curCard=curCard.next

    def getState(self):
        retStr=""
        curCard=self.top
        while curCard!=None:
            retStr+=str(curCard.value)+" "
            curCard=curCard.next
        retStr+="a"
        return retStr

    def getScore(self):
        curCard=self.top
        curScore=0
        curMult=self.length
        while curCard!=None:
            curScore+=curCard.value*curMult
            curMult-=1
            curCard=curCard.next
        return curScore

allDecks=[]
for line in decksFile:
    if "Player" in line:
        curDeck=Deck()
        allDecks+=[curDeck]
    elif line.strip("\n").isnumeric():
        curDeck.addCard(int(line.strip("\n")))

deck0=allDecks[0]
deck1=allDecks[1]
#
# while deck0.length!=0 and deck1.length!=0:
#     card0=deck0.drawCard()
#     card1=deck1.drawCard()
#     if(card0>card1):
#         deck0.addCard(card0)
#         deck0.addCard(card1)
#     else:
#         deck1.addCard(card1)
#         deck1.addCard(card0)
#
# print(deck1.getScore())
# print(deck0.getScore())
def playRecursively(deck0,deck1):
    #count=0
    roundNum=1
    allStates=set()
    while(deck0.length!=0 and deck1.length!=0):
        #print(deck0.getState()+deck1.getState())
        #print(allStates)
        #count+=1
        if str(deck0.getState()+deck1.getState()) in allStates:
            return 0
        allStates.add(str(deck0.getState()+deck1.getState()))
        #if(count>10):
         #   break
        card0=deck0.drawCard()
        card1=deck1.drawCard()
        #print("round",roundNum)
        roundNum+=1
        #print("player 1:",deck0.getState(),end="")
        #print("player 2:",deck1.getState(),end="")
        #print(card0,card1)
        if deck0.length>=card0 and deck1.length>=card1:
            newDeck0=deck0.copy(card0)
            newDeck1=deck1.copy(card1)
            if(playRecursively(newDeck0,newDeck1)==0):
                deck0.addCard(card0)
                deck0.addCard(card1)
            else:
                deck1.addCard(card1)
                deck1.addCard(card0)
        else:
            if(card0>card1):
                deck0.addCard(card0)
                deck0.addCard(card1)
            else:
                deck1.addCard(card1)
                deck1.addCard(card0)
    if(deck0.length==0):
        return 1
    else:
        return 0

playRecursively(deck0,deck1)
print(deck0.getScore())
print("----------")
print(deck1.getScore())
#deck1.printAllCards()
#deck0.printAllCards()