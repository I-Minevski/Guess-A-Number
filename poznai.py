import random

border=100
moves=0
computer_number=random.randint(1, border)
while True:
    player_input=input(f"Guess the number (1-{border}): ")
    if player_input.isdigit()==False:
        print("Invalid input. Try again.")
        player_input=input("Guess the number (1-100): ")
    else:
        player_guess=int(player_input)
        moves+=1
    if player_guess==computer_number:
        print("Correct!")
        answer=input("Do you want to play again? [y]es  [n]o ")
        if answer=="y":
            print("Level Up!")
            border+=100
            print(f"The range is now (1-{border})!")
            computer_number=random.randint(1, border)
            continue
        elif answer=="n":
            print(f"You made a total of {moves} moves. Good job!")
            break
        else:
            print("Invalid input. Try again.")
            answer=input("Do you want to play again? [y]es  [n]o ")
    if player_guess>computer_number:
        print("Too High!")
        continue
    if player_guess<computer_number:
        print("Too Low!")
        continue