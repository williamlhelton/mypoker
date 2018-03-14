from player import getPlayerSet
from engine.evaluations import evaluateHand
import engine.deck as deck
import engine.tablemanipulation as table
import random

def printGameState():
    print('{}\t{}\t{}\t{}\t{}\t{}'.format('NAME', 'POSITION', 'CHIPS', 'DEALER', 'HAND', 'QUALITY').expandtabs(12))
    for p in players:
        evaluated = evaluateHand(p.hand[0], p.hand[1])
        if p.isDealer == True:
            isCurrentDealer = 'button'
        else:
            isCurrentDealer = ''
        print(f'{p.name} \t(Seat {p.seat}) \t({p.chips}) \t{isCurrentDealer} \t{p.hand[0].shortString} {p.hand[1].shortString} \t{evaluated}'.expandtabs(12))

if __name__ == '__main__':
    # get a set of 9 players as a list so they can sit at the table in order
    players = list(getPlayerSet())
    for p in players:
        print(f'{p.name} joins the game!')

    # assign random dealer
    players[random.randint(0, 8)].isDealer = True

    # create game deck, shuffle it, and deal first hand
    gameDeck = deck.createDeck()
    deck.shuffle(gameDeck)
    print(gameDeck[0])
    table.dealHand(players, gameDeck)

    # print players and stats
    printGameState()

    # # print quality statements
    # for p in players:
    #     evaluated = evaluateHand(p.hand[0], p.hand[1])
    #     if evaluated == 'premium' or evaluated == 'great':
    #         print(f'{p.name} wants to raise')
    #     if evaluated == 'good':
    #         print(f'{p.name} wants to call')
    #     if evaluated == 'fine':
    #         print(f'{p.name} wants to check')
    #     if evaluated == 'trash':
    #         print(f'{p.name} wants to fold')
    
    # play hand
    table.playHand(players, gameDeck)
    printGameState()