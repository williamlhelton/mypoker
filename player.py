import random

def getTraits():
    traits = {
        'loose': bool(random.getrandbits(1)),
        'aggressive': bool(random.getrandbits(1)),
        'emotional': bool(random.getrandbits(1)),
        'lucky': bool(random.getrandbits(1))
    }
    return traits

def getName():
    # Possibly bad: reads all names into memory?
    # Better to get a number only?
    with open('firstnames.txt') as firstnames:
        names = firstnames.readlines()
    return random.choice(names)    

def getNameSet():
    names = set()
    counter = 9
    while counter >= 0:
        newName = getName()
        if newName in names:
            continue
        names.add(newName.rstrip())
        counter -= 1
    return names

def getPlayerSet():
    playerNameSet = getNameSet()
    players = [Player(name) for name in playerNameSet]
    return players

class Player:
    seat = 1
    def __init__(self, name):
        self.traits = getTraits()
        self.name = name
        self.seat = Player.seat
        Player.seat += 1
        self.chips = 1000
        self.hand = []
        self.isDealer = False
    def __str__(self):
        return '{}: {}'.format(self.name, self.traits)


if __name__ == '__main__':
    players = getPlayerSet()

    print([str(players[i]) for i, _ in enumerate(players)])

    print(f'{players[0].name} is loose: ', players[0].traits['loose'])
    print(f'{players[0].name} is aggressive: ', players[0].traits['aggressive'])
    print(f'{players[0].name} is emotional: ', players[0].traits['emotional'])
    print(f'{players[0].name} is lucky: ', players[0].traits['lucky'])

    print(f'{players[1].name} is loose: ', players[1].traits['loose'])
    print(f'{players[1].name} is aggressive: ', players[1].traits['aggressive'])
    print(f'{players[1].name} is emotional: ', players[1].traits['emotional'])
    print(f'{players[1].name} is lucky: ', players[1].traits['lucky'])
