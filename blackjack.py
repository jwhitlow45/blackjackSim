from sys import maxsize
import random as r
from typing import List

class Game:
    def __init__(self, numDecksInShoe: int):
        self.numDecksInShoe = numDecksInShoe
        self.count = 0
        
class Player:

    def decision(playerHand: List[int], dealerCard: int, count: int) -> int:
        """makes player decision based on player's hand, dealer's hand, and
        shoe count

        Args:
            playerHand (List[int]): player's hand
            dealerCard (List[int]): dealer's showing card
            count (int): count of current shoe

        Returns:
            int: player decision (0 = stand, 1 = hit, 2 = split)
        """
        

class Shoe:
    def __init__(self, numDecks: int):
        """shoe containing cards to be dealt from

        Args:
            numDecks (int): number of decks in the shoe
        """
        # contains all cards for a single suit of cards
        # A = 11, J,Q,K = 10
        self._single_suit = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        self.deck = []
        self.numDecks = numDecks
        for i in range(numDecks*4):
            self.deck += self._single_suit
            
    def deal(self):
        # 0 means inf deck so randomly pick from an inf deck
        if self.numDecks == 0:
            return self._single_suit[r.randint(0,len(self._single_suit))]
        return self.deck.pop()
        
    def shuffle():
        pass