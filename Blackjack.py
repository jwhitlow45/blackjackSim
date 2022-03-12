from sys import maxsize

class Game:
    def __init__(self, numDecksInShoe: int, numPlayerStartingChips: int, maxBet: int, numChipsToWin: int = maxsize):
        pass
    pass

class Player:
    def __init__(self, numChips: int):
        """init Player class

        Args:
            numChips (int): number of chips player has available for betting
        """
        self.numChips = numChips
        
    def bet(self, betSize: int):
        if betSize >= self.numChips:
            return betSize
        else:
            return -1
        

class Shoe:
    def __init__(self, numDecks: int):
        
        # contains all cards for a single deck of cards
        # A = 1, J = 11, Q = 12, K = 13
        _single_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
    def shuffle():
        pass