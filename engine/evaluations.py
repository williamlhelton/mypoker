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