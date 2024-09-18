import \
    random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(current_cards):
    """Returns a random card from the deck"""
    card = random.choice(deck)
    # Handle the ace
    if card == 11 and sum(current_cards) + card > 21:
        card = 1
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Start with 2 cards
user_cards = []
user_cards.append(deal_card(user_cards))
user_cards.append(deal_card(user_cards))

computer_cards = []

# Give the computer cards until he has more that 17
while sum(computer_cards) < 17:
    computer_cards.append(deal_card(computer_cards))

print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")

print(f"Computer's first card: {computer_cards[0]}")

user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

while user_should_deal == "y":
    user_cards.append(deal_card(user_cards))
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

if sum(user_cards) > 21:
    print("You went over. You lose 😭")
elif sum(computer_cards) > 21:
    print("Opponent went over. You win 😁")
elif sum(user_cards) == sum(computer_cards):
    print("Draw 🙃")
elif sum(user_cards) > sum(computer_cards):
    print("You win 😃")
else:
    print("You lose 😤")

    
