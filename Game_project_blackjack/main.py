from art import logo
import random


def deal_card():
    card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(card)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_name, c_score):
    if u_name == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_name == 0:
        return "Win with a Blackjack 😎"
    elif u_name > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_name > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or computer_score >21:
            is_game_over = True
        else:
            user_deal=input("Type 'y' to get another card,type 'n' to pass: ")
            if user_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(f"Your final hand:{user_card} , final score is {user_score}")
    print(f"Computer's final hand : {computer_card} ,final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 15)
    play_game()