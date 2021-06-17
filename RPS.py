import random

while True:
    user= input("Enter a choice \nrock\npaper\nscissors : ")
    actions = ["rock", "paper", "scissors"]
    computer = random.choice(actions)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Hurray!...Rock smashes scissors!\nYOU WIN!")
        else:
            print("Paper covers rock! You lose.\nBetter luck next time")
    elif user == "paper":
        if computer == "rock":
            print("Hurray!...Paper covers rock!\nYOU WIN!")
        else:
            print("Scissors cuts paper! You lose.\nBetter luck next time")
    elif user == "scissors":
        if computer == "paper":
            print("Hurray!...\nScissors cuts paper!\nYOU WIN!")
        else:
            print("Rock smashes scissors! You lose.\nBetter luck next time")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break