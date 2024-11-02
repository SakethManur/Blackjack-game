import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(score_user, score_dealer):
    if score_user == score_dealer:
        return "Draw"
    elif score_dealer == 0:
        return "Dealer has Blackjack, You Lose"
    elif score_user == 0:
        return "You have Blackjack, You Win"
    elif score_user > 21:
        return "You went over 21, You Lose"
    elif score_dealer > 21:
        return "Dealer went over 21, You Win"
    elif score_user > score_dealer:
        return "You Win"
    else:
        return "You Lose"

def game():
    global d_score, user_score
    user_card = []
    dealer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())

    print(art.logo)
    while not is_game_over:
        user_score = score(user_card)
        d_score = score(dealer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Dealer's card: {dealer_card[0]}")

        if user_score == 0 or d_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_new_card = input("Type 'y' to get a new card or 'n' to pass: ")
            if user_new_card == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while d_score != 0 and d_score < 17:
        dealer_card.append(deal_card())
        d_score = score(dealer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_card}, final score: {d_score}")
    print(compare(user_score, d_score))

while input("Do you want to play a game of Blackjack? If yes, type 'y' or type 'n' for no: ") == "y":
    game()
    print("\n" * 9)

