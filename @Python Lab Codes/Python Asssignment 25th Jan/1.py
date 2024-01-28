import random
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
# Part 1
def create_deck():
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def deal_hand(deck):
    print("Dealing ...")
    hand = random.sample(deck, 5)
    for card in hand:
        deck.remove(card)
    return hand

def display_deck(deck):
    print(deck)
    print(f"There are {len(deck)} cards in the deck.")

# Part 2
deck = create_deck()
display_deck(deck)
hand = deal_hand(deck)
print(f"There are {len(deck)} cards in the deck.")
print("Player has the following cards in their hand:")
print(hand)

# Part 3
try:
    with open("Text1.txt", "w") as file:
        deck = create_deck()
        for card in deck:
            file.write(card + "\n")
    print(f"Total number of lines in Text1.txt: {len(deck)}")

    with open("Text1.txt", "r") as file:
        cards_dict = {i: line.strip() for i, line in enumerate(file)}
        print(cards_dict)

except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Part 4
try:
    with open("Text1.txt", "r") as file:
        cards_list_of_tuples = [(i, line.strip()) for i, line in enumerate(file)]
        print(cards_list_of_tuples)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
