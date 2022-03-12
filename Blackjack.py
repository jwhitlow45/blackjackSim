from sys import maxsize
from typing import List

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
        self.count = 0
        
    def bet(self, betSize: int) -> int:
        """bets funds for player, fails if bet is larger than number of chips

        Args:
            betSize (int): size of player bet

        Returns:
            int: returns size of bet, if bet too large returns -1
        """
        if betSize >= self.numChips:
            self.numChips -= betSize
            return betSize
        else:
            return -1
        
    def decision(playerHand: List[int], dealerHand: List[int]) -> str:
        pass
        

class Shoe:
    def __init__(self, numDecks: int):
        
        # contains all cards for a single deck of cards
        # A = 1, J = 11, Q = 12, K = 13
        _single_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        
    
    def shuffle():
        pass