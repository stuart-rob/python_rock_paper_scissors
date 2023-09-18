import random #importing the random function
user_score = 0
computer_score = 0


while True:
    
    user_choice = input("rock, paper, scissors?")
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"IT'S A TIE")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print(f"ROCK KILLS SCISSORS, YOU WIN!")
            user_score += 1
        else:
            print(f"PAPER COVERS ROCK, YOU LOSE!")
            computer_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print(f"PAPER COVERS ROCK, YOU WIN!")
            user_score += 1
        else:
            print(f"SCISSORS KILL PAPER, YOU LOSE!")
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print(f"SCISSORS KILL PAPER, YOU WIN!")
            user_score += 1
        else:
            print(f"ROCK KILLS SCISSORS, YOU LOSE!")
            computer_score += 1
    
    play_again = input("Fart again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Your final score is " + str(user_score))
print("Computer's final score is " + str(computer_score))
if user_score > computer_score:
    print("YOU ARE THE OVERALL WINNER")
elif computer_score > user_score:
    print("You lost")
    
