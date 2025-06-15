import random
import os
from time import sleep
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

newGame = True

def calc_hand_score(hand):
    value = sum(hand)

    aces = hand.count(11)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (posix)
    else:
        os.system('clear')

while newGame:
    clear_screen()
    continueGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continueGame == "n":
        newGame = False
    elif continueGame == "y":
        user_hand = [random.choice(cards), random.choice(cards)]
        user_score = calc_hand_score(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        computer_hand = [random.choice(cards), random.choice(cards)]
        computer_score = calc_hand_score(computer_hand)
        print(f"Dealers's first card: {computer_hand[0]}")
        if user_score == 21 and computer_score != 21:
            print("You hit blackjack. YOU WIN")
            print(f"Your hand: {user_hand}, final score{user_score}")
            print(f"Dealer's Hand: {computer_hand}, final score{computer_score}")
            continue
        elif computer_score == 21 and user_score != 21:
            print("The dealer hit blackjack. You LOSE")
            print(f"Your hand: {user_hand}, final score{user_score}")
            print(f"Dealer's Hand: {computer_hand}, final score{computer_score}")
            continue
        elif user_score == 21 and computer_score == 21:
            print("Both got blackjack. It's a DRAW!")
            print(f"Your hand: {user_hand}, final score{user_score}")
            print(f"Dealer's Hand: {computer_hand}, final score{computer_score}")
            continue
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        while draw == 'y':
            user_hand.append(random.choice(cards))
            user_score = calc_hand_score(user_hand)
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Dealers's first card: {computer_hand[0]}")
            if user_score > 21:
                print(f"Your final hand: {user_hand}, final score {user_score}")
                print(f"Dealers's final hand: {computer_hand}")
                print("You went over. You lose!")
                break
            draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == 'n' and user_score <= 21:
            computer_score = calc_hand_score(computer_hand)
            user_score = calc_hand_score(user_hand)
            while computer_score < user_score:
                computer_hand.append(random.choice(cards))
                computer_score = calc_hand_score(computer_hand)
            if computer_score > 21:
                print("The dealer went over you win!")
            elif computer_score == user_score:
                print("Its a draw!")
            elif computer_score > user_score:
                print("You lose!")
            else:
                print("You win!")
            print(f"Your final hand: {user_hand}, final score {user_score}")
            print(f"Dealer's final hand: {computer_hand}, final score: {computer_score}")
    sleep(3)
