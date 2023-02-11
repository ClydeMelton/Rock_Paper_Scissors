import random

while True:
    print("Welcome challenger, let us play the ancient game of rock, paper, scissors\n")
    
    print("Choose your weapon. Rock, paper, or scissors")

    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    player_choice = input("\n").lower()
    print(f"You chose {player_choice}, and I chose {computer_choice}\n")


    if player_choice == "rock":
        if computer_choice == "paper":
            print("You have lost this time.\n")
        elif computer_choice == "rock":
            print("Oh no, we tied\n")
        else:    
            print("You have bested me this time.\n")   
            
    if player_choice == "paper":
        if computer_choice == "scissors":
            print("You have lost this time.\n")
        elif computer_choice == "paper":
            print("Oh no, we tied\n")
        else:
            print("You have bested me this time.\n")    
            
    if player_choice == "scissors":
        if computer_choice == "rock":
            print("You have lost this time.\n")
        elif computer_choice == "scissors":
            print("Oh no, we tied\n")
        else:
            print("You have bested me this time.\n")
    print("\nWould you like to play again?: Yes or No. \n")
    replay = input("").lower()
    if replay == "no":
        break

