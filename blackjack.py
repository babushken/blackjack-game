"""
Blackjack Terminal Game
Description: A terminal-style blackjack game.
Author: babushken
"""

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def display(self):
        suits_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
        suit_symbol = suits_symbols.get(self.suit, '?')
        value_display = self.value if len(self.value) == 2 else f" {self.value}"
        return f"""
 _______
|{value_display}     |
|   {suit_symbol}   |
|     {value_display}|
 -------
"""

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
                for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt.")
        return self.cards.pop()

def test_cards():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '5', '9', 'J', 'Q', 'K', 'A', '10']
    
    cards = [Card(suit, value) for suit in suits for value in values]  # Sample 8 cards
    
    for card in cards:
        print(card.display())

def test_deck():
    deck = Deck()
    print("Deck shuffled. Dealing cards...\n")
    for _ in range(5):  # Deal 5 cards to test
        card = deck.deal()
        print(card.display())

if __name__ == "__main__":
    #test_cards()
    test_deck()