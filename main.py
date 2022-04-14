import blackjack as bl
"""
Decision policies:
1.= if your hand >= 17, stick, else hit
2 = if your hand >= 17 and is hard, stick, else hit unless your hand = 21
4 = always stand
"""


def main():
    numDecksList = [0, 1]
    playerPolicyList = [1, 2, 4]
    numGames = 1000000

    # store results to write to csv at end
    lines = []
    header = 'num decks,player policy,num games,player wins,dealer wins,total games,player win %\n'
    lines.append(header)
    for numDecks in numDecksList:
        for playerPolicy in playerPolicyList:
            curGame = bl.Game(numDecks)

            dealerWins = 0
            playerWins = 0

            for i in range(numGames):
                if curGame.play(1) == True:
                    playerWins += 1
                else:
                    dealerWins += 1

            line = f'{numDecks},{playerPolicy},{numGames},{playerWins},{dealerWins},{numGames},{playerWins/numGames}\n'
            lines.append(line)

    with open('results.csv', 'w') as FILE:
        FILE.writelines(lines)


if __name__ == '__main__':
    main()
