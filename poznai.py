import random

computer_number=random.randint(1, 100)
while True:
    player_input=input("Guess the number (1-100): ")
    if player_input.isdigit()==False:
        print("Invalid input. Try again.")
        player_input=input("Guess the number (1-100): ")
    else:
        player_guess=int(player_input)
    if player_guess==computer_number:
        print("Correct!")
        answer=input("Do you want to play again? [y]  [n]")
        if answer=="y":
            continue
        elif answer=="n":
            break
        else:
            print("Invalid input. Try again.")
            answer=input("Do you want to play again? [y]  [n]")
    if player_guess>computer_number:
        print("Too High!")
        continue
    if player_guess<computer_number:
        print("Too Low!")
        continue