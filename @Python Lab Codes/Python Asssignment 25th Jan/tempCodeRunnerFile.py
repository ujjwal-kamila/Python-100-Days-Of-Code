# Part 2: Create and display the initial deck, deal a hand, and display the updated deck
deck = create_deck()
display_deck(deck)
hand = deal_hand(deck)
print(f"There are {len(deck)} cards in the deck.")
print("Player has the following cards in their hand:")
print(hand