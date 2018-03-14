from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.shortString = self.getShortString()
        self.numvalue = self.getNumValue()
    def __str__(self):
        return f'{self.value} of {self.suit}'
    def getShortString(self):
        shortString = ''
        if self.value in ('ace', 'jack', 'queen', 'king'):
            shortString += self.value[0].upper()
        elif self.value == '10':
            shortString += 'T'
        else:
            shortString += self.value
        
        shortString += self.suit[0]
        return shortString
    def getNumValue(self):
        if(self.value == 'ace'):
            return 14
        if(self.value == 'king'):
            return 13
        if(self.value == 'queen'):
            return 12
        if(self.value == 'jack'):
            return 11
        return int(self.value)

def createDeck():
    "create one 52-card, unshuffled deck"
    deck = []
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    [deck.append(Card(v, s)) for v in values for s in suits]
    return deck

# drawCard rotates the first card to the bottom of the deck
# no cases should cause repeat cards and this keeps the deck intact
def drawCard(deck):
    "return one card from the top of the deck"
    card = deck[0]
    deck[:] = deck[1:] + deck[:1]
    return card

if __name__ == '__main__':
    myDeck = createDeck()
    shuffle(myDeck)
    a = drawCard(myDeck)
    print(f'a: {a}')
    b = drawCard(myDeck)
    print(f'b: {b}')
    print('')
    print(f'{a.numvalue} > {b.numvalue}?: ', a.numvalue > b.numvalue)
    print(f'{b.numvalue} > {a.numvalue}?: ', b.numvalue > a.numvalue)
    print(f'{a.numvalue} < {b.numvalue}?: ', a.numvalue < b.numvalue)
    print(f'{b.numvalue} < {a.numvalue}?: ', b.numvalue < a.numvalue)
    print(f'{b.numvalue} == {a.numvalue}?: ', b.numvalue == a.numvalue)