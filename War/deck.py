#!/usr/bin/env python3
from random import shuffle
'''Creating a reusable deck for other games'''

class Card:
    #create cards for the game
    suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 
                    'Spades': '\u2660', 'Clubs': '\u2663'}
    

    def __init__(self, rank, suit): #rank, suit
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        letters = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
        letter = letters.get(self.rank, str(self.rank))
        suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 
                    'Spades': '\u2660', 'Clubs': '\u2663'}
        suit = suits.get(self.suit, str(self.suit))
        return "{0} of {1}".format(letter, suit)
        deck = [Card(rank, suit) for rank in range(1,14) for suit in suits]

class Deck:
    def create_deck(self):
        suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 
                    'Spades': '\u2660', 'Clubs': '\u2663'}
        global deck
        deck = [Card(rank, suit) for rank in range(1,14) for suit in suits]

    def shuffle_deck(deck):
        
        deck = shuffle(deck)
        return deck

    # create_deck()
    # shuffle_deck(deck)
# class Card2:
#     def __init__(self, value, suit):
#         self.value = value
#         self.suit = suit
    
#     def __repr__(self):
#         letters = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
#         letter = letters.get(self.value, str(self.value))
#         suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 
#                     'Spades': '\u2660', 'Clubs': '\u2663'}
#         suit = suits.get(self.suit, str(self.suit))
#         return "<Cards {0} of {1}>".format(letter, suit)
        


