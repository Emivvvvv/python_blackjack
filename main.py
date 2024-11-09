import random

# Define the deck of cards with symbols for suits
suits = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Build the deck by combining suits and ranks
deck = [{'suit': suit, 'rank': rank, 'value': values[rank]} for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal a card from the deck
def deal_card():
    return deck.pop()

# Calculate the total value of a hand, adjusting for Aces
def calculate_hand_value(hand):
    value = sum(card['value'] for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'Ace')

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

# Display hand in a decorated format with symbols and current value
def display_hand(hand, is_dealer=False):
    hand_str = ""
    for card in hand:
        hand_str += f"[{card['rank']} {suits[card['suit']]}] "
    hand_value = calculate_hand_value(hand)
    if is_dealer:
        print(f"Dealer's hand: {hand_str}({hand_value})")
    else:
        print(f"Your hand: {hand_str}({hand_value})")

# Main Blackjack game function
def play_blackjack():
    # Initial hands for player and dealer
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    display_hand(player_hand)
    first_dealer_card = dealer_hand[0]
    print(f"Dealer's showing: [{first_dealer_card['rank']} {suits[first_dealer_card['suit']]}]")

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to [H]it or [S]tand? ").strip().lower()

        if action == 'h':
            player_hand.append(deal_card())
            display_hand(player_hand)
        else:
            break

    # Calculate final hand values
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # Dealer's turn (hits until reaching at least 17)
    while dealer_value < 17:
        dealer_hand.append(deal_card())
        dealer_value = calculate_hand_value(dealer_hand)

    print("\nFinal Results:")
    display_hand(player_hand)
    display_hand(dealer_hand, is_dealer=True)

    # Determine the winner
    if player_value > 21:
        print("You bust! Dealer wins.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value == dealer_value:
        print("It's a tie!")
    else:
        print("Dealer wins.")

# Start the game
play_blackjack()
