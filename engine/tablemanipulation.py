# actions when game is running
# create casino tables
# deal cards to players at tables
import engine.deck as deck
from engine.evaluations import evaluateHand

def dealHand(players, gameDeck):
    "deals 2 cards to each player"
    for p in players:
        p.hand.append(deck.drawCard(gameDeck))
    for p in players:
        p.hand.append(deck.drawCard(gameDeck))

def playHand(players, gameDeck):
    "plays a hand after all cards have been dealt"
    # find dealer
    for p in players:
        if p.isDealer:
            dealer = p
            break

    print(f"the dealer is {dealer.name}")
    
    # pass over small and big blind and force them to post
    # responding to the big blind is the first action
    currentPlayer = getNextPlayer(players, dealer)
    postBlinds(currentPlayer, "small")
    print(f"the small blind is {currentPlayer.name}")

    currentPlayer = getNextPlayer(players, currentPlayer)
    postBlinds(currentPlayer, "big")
    print(f"the big blind is {currentPlayer.name}")
    actionOn = currentPlayer
    action = ('raise', 10)
    print("action[0] = " + str(action[0]))

    currentPlayer = getNextPlayer(players, currentPlayer)
    print(f"the first player to act is {currentPlayer.name}")
    
    # wait until action has gone all the way around the table
    while actionOn != currentPlayer:
        if len(players) == 1:
            print(f'{players[0].name} is the last player and wins')
            break

        returnAction = playerResponse(currentPlayer, action)
        if str(returnAction[0]) == "fold":
            oldPlayer = currentPlayer
            currentPlayer = getNextPlayer(players, currentPlayer)
            players.remove(oldPlayer)
        elif str(returnAction[0]) == "raise":
            actionOn = currentPlayer
            action = returnAction
            currentPlayer = getNextPlayer(players, currentPlayer)
        elif str(returnAction[0]) == "allin":
            actionOn = currentPlayer
            action = returnAction
            oldPlayer = currentPlayer
            currentPlayer = getNextPlayer(players, currentPlayer)
            players.remove(oldPlayer)
        else:
            currentPlayer = getNextPlayer(players, currentPlayer)
    
    print(f"all players have acted")

def getNextPlayer(players, currentPlayer):
    "returns next player in sequence"
    indexOfPlayer = players.index(currentPlayer)
    if currentPlayer == players[-1]:
        indexOfPlayer = 0
    else:
        indexOfPlayer += 1
    return players[indexOfPlayer]

def postBlinds(player, blindType):
    if blindType == "small":
        player.chips -= 5
    if blindType == "big":
        player.chips -= 10

def playerResponse(player, action):
    "decide a player action based on chip count, bet size and hand quality"
    evaluated = evaluateHand(player.hand[0], player.hand[1])
    if action[0] == "raise":
        if (evaluated == "premium" or evaluated == "great") and player.chips >= action[1]:
            betAmount = playerAllIn(player)
            return ("allin", betAmount)
        elif evaluated == "good" and player.chips >= action[1]:
            playerCall(player, action[1])
            return ("call", action[1])
        elif player.chips <= action[1]:
            betAmount = playerAllIn(player)
            return ("allin", betAmount)
        else:
            playerFold(player)
            return ("fold",)
    else:
        playerFold(player)
        return ("fold",)


def playerBet(player):
    # if player.chips <= 100:
    #     betAmount = player.chips
    #     print(f'{player.name} goes all in with {player.chips}')
    #     player.chips = 0
    #     return ("raise", betAmount)
    pass

def playerCall(player, betAmount):
    print(f'{player.name} calls with {betAmount}')
    player.chips -= betAmount

def playerAllIn(player):
    betAmount = player.chips
    print(f'{player.name} goes all in with {player.chips}')
    player.chips = 0
    return betAmount

def playerFold(player):
    print(f'{player.name} folds')

if __name__ == '__main__':
    pass