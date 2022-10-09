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
        break
    if player_guess>computer_number:
        print("Too High!")
        continue
    if player_guess<computer_number:
        print("Too Low!")
        continue