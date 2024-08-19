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

class Player:
    def __init__(self):
        self.hand = []
        self.money = 888
    
    def add_card(self, card):
        self.hand.append(card)
    
    def show_hand(self):
        return '\n'.join(card.display() for card in self.hand)
    
    def total_value(self):
        value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        total = 0
        aces = 0

        for card in self.hand:
            total += value_map[card.value]
            if card.value == 'A':
                aces += 1
        
        while total > 21 and aces:
            total -= 10
            aces -= 1
        
        return total
    
    def take_turn(self, deck):
        while True:
            print(f"Your hand:\n{self.show_hand()}\nTotal value: {self.total_value()}")
            action = input("Choose action: (h)it, (s)tand: ").lower()
            
            if action == 'h':
                self.add_card(deck.deal())
                if self.total_value() > 21:
                    print(f"Busted! Your hand value: {self.total_value()}")
                    break
            elif action == 's':
                break
            else:
                print("Invalid action. Please choose 'h' to hit or 's' to stand.")

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

def test_player():
    deck = Deck()
    player = Player()
    
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    print("Player's turn:")
    player.take_turn(deck)
    print(f"Final hand:\n{player.show_hand()}\nTotal value: {player.total_value()}")

if __name__ == "__main__":
    #test_cards()
    #test_deck()
    test_player()