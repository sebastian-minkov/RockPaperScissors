import random

rock = "rock"
paper = "paper"
scissors = "scissors"

player_score = 0
computer_score = 0

game_on = "y"

while game_on == "y":

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Please try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print("\033[0;32m" + "You win!")
        player_score += 1
    elif player_move == computer_move:
        print("\033[1;33m" + "Draw!")
    else:
        print("\033[0;31m" + "You lose!")
        computer_score += 1

    print("\033[0m")
    print(f"Current score: Player - {player_score} / Computer - {computer_score}")

    game_on = input("Type [y]es to play again or any key to quit: ")
