from player import getPlayerSet
import engine.deck as deck

def dealHand(players, gameDeck):
    for p in players:
        p.hand.append(deck.drawCard(gameDeck))
    for p in players:
        p.hand.append(deck.drawCard(gameDeck))

def evaluateHand(card1, card2):
    values = {card1.value, card2.value}
    suits = {card1.suit, card2.suit}
    # *** PREMIUM ***
    # AA, (AK-suited AK-offsuit), KK, QQ, AQ-suited
    if (len(values) == 1 and ('ace' in values or 'king' in values or 'queen' in values)) or ('ace' in values and 'king' in values):
        return 'premium'
    # *** GREAT ***
    # T or higher, pocket 6s or higher
    if (card1.numvalue >= 10 and card2.numvalue >= 10) or (card1.numvalue >= 6 and card1.value == card2.value):
        return 'great'
    # *** GOOD ***
    # Ax Kx suited, suited connectors, low pairs
    if (
        ((card1.value == 'ace' or card2.value == 'ace' or card1.value == 'king' or card2.value == 'king') and len(suits) == 1) or
        (abs(card1.numvalue-card2.numvalue) <= 2 and len(suits) == 1) or
        (card1.value == card2.value)
        ):
        return 'good'
    # *** FINE ***
    # Ax Kx offsuit, Q+half offsuit, suited xx
    if ((card1.value == 'ace' or card2.value == 'ace' or card1.value == 'king' or card2.value == 'king') or (len(suits) == 1) or
        'queen' in values and card1.numvalue > 7 and card2.numvalue > 7
        ):
        return 'fine'
    # *** TRASH ***
    # everything else
    return 'trash'


if __name__ == '__main__':
    players = getPlayerSet()
    for p in players:
        print(f'{p.name} joins the game!')
    gameDeck = deck.createDeck()
    deck.shuffle(gameDeck)
    # print(gameDeck[0])
    dealHand(players, gameDeck)

    print('{}\t{}\t{}\t{}\t{}'.format('NAME', 'POSITION', 'CHIPS', 'HAND', 'QUALITY').expandtabs(12))
    for p in players:
        evaluated = evaluateHand(p.hand[0], p.hand[1])
        print(f'{p.name} \t(Seat {p.seat}) \t({p.chips}) \t{p.hand[0].shortString} {p.hand[1].shortString} \t{evaluated}'.expandtabs(12))

    for p in players:
        evaluated = evaluateHand(p.hand[0], p.hand[1])
        if evaluated == 'premium' or evaluated == 'great':
            print(f'{p.name} wants to raise')
        if evaluated == 'good':
            print(f'{p.name} wants to call')
        if evaluated == 'fine':
            print(f'{p.name} wants to check')
        if evaluated == 'trash':
            print(f'{p.name} wants to fold')
