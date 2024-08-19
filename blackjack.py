"""
a terminal-style blackjack game.
made by babushken.
"""

import random

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(suit, rank) for suit in suits for rank in ranks]

def card_value(rank):
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

def hand_value(hand):
    value = sum(card_value(rank) for suit, rank in hand)
    num_aces = sum(1 for suit, rank in hand if rank == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def draw_card(deck):
    return deck.pop()

def initial_deal(deck):
    return [draw_card(deck), draw_card(deck)]

def print_card(card):
    suit, rank = card
    if rank == '10':
        rank_str = "10"
    else:
        rank_str = rank.ljust(2)  # Adjusting for alignment

    card_str = (
        f"-----\n"
        f"| {rank_str}|\n"
        f"| {suit} |\n"
        f"-----"
    )
    return card_str

def print_hand(hand, hidden=False):
    if hidden:
        card_strs = [print_card(hand[1])]  # Only show the second card (hidden)
        card_strs.insert(0, "-----\n| Hidden Card |")
    else:
        card_strs = [print_card(card) for card in hand]
    
    card_rows = [card.split('\n') for card in card_strs]

    spacing = 2
    
    lines = []
    for i in range(len(card_rows[0])):
        line = ""
        for row in card_rows:
            line += row[i].ljust(len(row[i]) + spacing)
        lines.append(line.rstrip())
    
    return "\n".join(lines)

def print_header(text):
    print(f"\n{'='*len(text)}\n{text}\n{'='*len(text)}")

def print_game_state(player_hand, dealer_hand, is_dealer_hidden=True):
    print_header("Your Hand")
    print(print_hand(player_hand))
    print(f"Value: {hand_value(player_hand)}\n")
    
    if is_dealer_hidden:
        print_header("Dealer's Hand")
        print(print_hand([dealer_hand[0], ('?', '?')]))  # Dealer's hidden card
    else:
        print_header("Dealer's Hand")
        print(print_hand(dealer_hand, hidden=False))
        print(f"Value: {hand_value(dealer_hand)}\n")

def blackjack_game():
    money = 1000
    print_header("Welcome to Blackjack!")

    while money > 0:
        deck = create_deck()
        random.shuffle(deck)
        player_hand = initial_deal(deck)
        dealer_hand = initial_deal(deck)

        bet = int(input(f"You have ${money}. Enter your bet: "))
        if bet > money:
            print("Bet cannot be more than your current money.")
            continue

        print_game_state(player_hand, dealer_hand)

        # Player's turn
        while hand_value(player_hand) < 21:
            action = input("Do you want to (h)it, (s)tand, or (d)ouble down? ").lower()
            if action == 'h':
                player_hand.append(draw_card(deck))
                print_game_state(player_hand, dealer_hand, is_dealer_hidden=True)
            elif action == 's':
                break
            elif action == 'd':
                bet *= 2
                player_hand.append(draw_card(deck))
                print_game_state(player_hand, dealer_hand, is_dealer_hidden=True)
                break
            else:
                print("Invalid input. Please enter 'h', 's', or 'd'.")

        if hand_value(player_hand) > 21:
            print_header("Player Busts!")
            print_game_state(player_hand, dealer_hand, is_dealer_hidden=False)
            money -= bet
        else:
            # Dealer's turn
            print_game_state(player_hand, dealer_hand, is_dealer_hidden=False)
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(draw_card(deck))
                print_game_state(player_hand, dealer_hand, is_dealer_hidden=False)

            # Determine winner
            player_value = hand_value(player_hand)
            dealer_value = hand_value(dealer_hand)

            if dealer_value > 21 or player_value > dealer_value:
                print_header("Player Wins!")
                money += bet
            elif player_value < dealer_value:
                print_header("Dealer Wins!")
                money -= bet
            else:
                print_header("It's a Tie!")

        # Display user's money after the round
        print(f"Your current balance: ${money}")

        if money > 0:
            if input("Do you want to play again? (y/n) ").lower() != 'y':
                break

    print_header(f"Game Over! You ended with ${money}")

if __name__ == "__main__":
    blackjack_game()
