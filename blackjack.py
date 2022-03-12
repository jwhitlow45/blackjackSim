from sys import maxsize
import random as r
from typing import List

class Game:
    def __init__(self, numDecksInShoe: int):
        self.numDecksInShoe = numDecksInShoe
        self.count = 0
        
class Player:
    def decision_policy_1(cls, hardCount: int, softCount: int) -> int:
        """if your hand >= 17, stick, else hit

        Args:
            hardCount (int): value of player's hand (ace = 1)
            softCount (int): value of player's hand (ace = 11)

        Returns:
            int: player decision (0 = stand, 1 = hit)
        """
        stopValue = 17
        if hardCount >= stopValue or softCount >= stopValue:
            return 0
        else:
            return 1
    
    def decision_policy_2(cls, hardCount: int, softCount: int) -> int:
        """if your hand >= 17 and is hard, stick, else hit unless your hand = 21

        Args:
            hardCount (int): value of player's hand (ace = 1)
            softCount (int): value of player's hand (ace = 11)

        Returns:
            int: player decision (0 = stand, 1 = hit)
        """
        if hardCount >= 17 or softCount == 21:
            return 0
        else:
            return 1
    
    def decision_policy_4(cls) -> int:
        """always stand

        Returns:
            int: decision to stand (0 = stand)
        """
        return 0

    def decision_card_count(cls, playerHand: List[int], dealerCard: int,
                            shoeCount: int, hardCount: int, softCount: int) -> int:
        """makes player decision based on player's hand, dealer's hand, and
        shoe count

        Args:
            playerHand (List[int]): player's hand
            dealerCard (List[int]): dealer's showing card
            shoeCount (int): count of current shoe
            hardCount (int): value of player's hand (ace = 1)
            softCount (int): value of player's hand (ace = 11)

        Returns:
            int: player decision (0 = stand, 1 = hit, 2 = split)
        """
        pass

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
        # populate deck
        for i in range(numDecks*4):
            self.deck += self._single_suit
        # shuffle deck
        self.shuffle()
            
    def deal(self) -> int:
        """deal card from shoe, if number of decks is 0 draw from inf deck

        Returns:
            int: card from shoe
        """
        if self.numDecks == 0:
            return self._single_suit[r.randint(0,len(self._single_suit - 1))]
        return self.deck.pop()
        
    def shuffle(self) -> None:
        """shuffle deck in shoe
        """
        r.shuffle(self.deck)