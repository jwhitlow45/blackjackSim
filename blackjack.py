from sys import maxsize
import random as r
from typing import List

class Game:
    def __init__(self, numDecksInShoe: int):
        self.numDecksInShoe = numDecksInShoe
        
    def play(self, decisionPolicy) -> bool:
        """game loop for playing blackjack

        Returns:
            bool: result of game, 0 if house wins, 1 if player wins
        """
        curShoe = Shoe(self.numDecksInShoe)
        
        playerHand = []
        dealerHand = []
        
        playerHardCount = None
        playerSoftCount = None
        dealerSoftCount = None
        
        # deal two cards each to player and dealer
        for i in range(2):
            playerHand.append(curShoe.deal())
            dealerHand.append(curShoe.deal())
            
        # player plays
        while True:                
            # get soft and hard player hand counts
            playerHardCount = self.calc_hard_count(playerHand)
            playerSoftCount = self.calc_soft_count(playerHand)
            
            if playerHardCount > 21:
                return False
            
            decision = -1
            if decisionPolicy == 1:
                decision = Player.decision_policy_1(Player, playerHardCount, playerSoftCount)
            elif decisionPolicy == 2:
                decision = Player.decision_policy_2(Player, playerHardCount, playerSoftCount)
            elif decisionPolicy == 3:
                decision = Player.decision_policy_3(Player)
            elif decisionPolicy == 4:
                decision = Player.decision_policy_4(Player, playerHardCount, playerSoftCount, dealerHand[0])
            elif decisionPolicy == 5:
                decision = Player.decision_policy_5(Player, playerHand)
                
            if decision == 0:
                break
            elif decision == 1:
                playerHand.append(curShoe.deal())
           
        # dealer plays     
        while True:
            # get soft dealer hand count
            dealerSoftCount = self.calc_soft_count(dealerHand)
            
            if dealerSoftCount > 21:
                return True
            if dealerSoftCount == 21:
                return False
            
            # dealer decision
            decision = Dealer.decision_policy_soft17(Dealer, dealerSoftCount)
            
            if decision == 0:
                break
            elif decision == 1:
                dealerHand.append(curShoe.deal())
                
        # if dealer hand is less player wins
        if dealerSoftCount < playerHardCount:
            return True
        if dealerSoftCount < playerSoftCount and playerSoftCount <= 21:
            return True
        return False
            
    def calc_hard_count(self, hand: List[int]) -> int:
        """returns hard count (a=1) of given hand

        Args:
            hand (List[int]): hand card

        Returns:
            int: hard count of given hand
        """
        handCount = 0
        for card in hand:
            if card == 11:
                handCount += 1
            else:
                handCount += card
        return handCount
        
    def calc_soft_count(self, hand: List[int]) -> int:
        """returns soft count (a=11) of given hand

        Args:
            hand (List[int]): card hand

        Returns:
            int: soft count of given hand
        """
        return sum(hand)
        
        
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
        if softCount > 21:
            if hardCount >= stopValue:
                return 0
            else:
                return 1
        else:
            if softCount >= stopValue:
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
    
    def decision_policy_3(cls) -> int:
        """always stand

        Returns:
            int: decision to stand (0 = stand)
        """
        return 0
    
    def decision_policy_4(cls, hardCount: int, softCount: int, dealerUpCard: int) -> int:
        """set stop value at 19 if dealer up card is an ace or face card else
        set stop value at 17

        Args:
            hardCount (int): value of player's hand (ace = 1)
            softCount (int): value of player's hand (ace = 11)
            dealerUpCard (int): dealers card that player can see

        Returns:
            int: player decision (0 = stand, 1 = hit)
        """
        
        stopValue: int
        if dealerUpCard == 10 or dealerUpCard == 11:
            stopValue = 19
        else:
            stopValue = 17
            
        if softCount > 21:
            if hardCount >= stopValue:
                return 0
            else:
                return 1
        else:
            if softCount >= stopValue:
                return 0
            else:
                return 1
        
    def decision_policy_5(cls, playerHand: List[int]) -> int:
        """hit once then stand
        Args:
            playerHand (List[int]): list of cards in player's hand

        Returns:
            int: player decision (0 = stand, 1 = hit)
        """
        
        if len(playerHand) > 2:
            return 0
        return 1
        

        
    
class Dealer:
    def decision_policy_soft17(cls, softCount: int):
        """decision made by dealer

        Args:
            softCount (int): value of dealer's hand (ace = 11)

        Returns:
            int: dealer decision (0 = stand, 1 = hit)
        """
        if softCount < 17:
            return 1
        return 0
        

class Shoe:
    def __init__(self, numDecks: int):
        """shoe containing cards to be dealt from

        Args:
            numDecks (int): number of decks in the shoe
        """
        # contains all cards for a single suit of cards
        # A = 11, J,Q,K = 10
        self._single_suit = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        self.deck: List
        self.numDecks = numDecks
        # set up shoe
        self.populate_shoe()
        # shuffle deck
        self.shuffle()
        
    def populate_shoe(self) -> None:
        """remove all cards from shoe and place proper number of cards in shoe
        based on number of decks in shoe
        """
        # clear out deck
        self.deck = list()
        # populate deck
        for i in range(self.numDecks*4):
            self.deck += self._single_suit
            
    def deal(self) -> int:
        """deal card from shoe, if number of decks is 0 draw from inf deck

        Returns:
            int: card from shoe
        """
        if self.numDecks == 0:
            return self._single_suit[r.randint(0,len(self._single_suit) - 1)]
        return self.deck.pop()
        
    def shuffle(self) -> None:
        """shuffle deck in shoe
        """
        r.shuffle(self.deck)