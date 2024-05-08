from Art import logo, vs
from game_data import data
import random

def player_choice():
    while True:
        player_choice = input("Who has more followers? Type 'A' or 'B':  ").lower()
        if player_choice in ['a', 'b']:
            return player_choice
        else:
            print("Invalid input. Please type 'A' or 'B'!")

def display_choice_a(choice):
    return f"Compare A: {choice['name']}, a {choice['description']}, from {choice['country']}."
def display_choice_b(choice):
    return f"Against B: {choice['name']}, a {choice['description']}, from {choice['country']}."
def game():
    score = 0
    print(logo)

    while True:
        random_a = random.choice(data)
        random_b = random.choice(data)
        print(display_choice_a(random_a))
        print(vs)
        print(display_choice_b(random_b))
        player = player_choice()

        if (random_a['follower_count'] > random_b['follower_count'] and player == "a") or \
                (random_b['follower_count'] > random_a['follower_count'] and player == "b"):
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    while True:
        try_again = input("Do you want to try again? Type 'yes' or 'no': ").lower()
        if try_again == "yes":
            game()
        elif try_again == "no":
            print("Thank you for playing! Have a wonderful day!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'!")

game()