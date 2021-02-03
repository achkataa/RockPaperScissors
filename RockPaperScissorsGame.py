import random

computer_points = 0
achkata_points = 0

while True:


    print("Choose from the list:"
      " Rock, Paper, Scissors")
    player_option = input()
    print(f"Your choice is {player_option}")


    computer_options = ["Rock", "Paper", "Scissors"]

    computer_option = random.choice(computer_options)
    print(f"Computer choice is {computer_option}")


    if player_option == "Rock":
        if computer_option == "Rock":
            print("It is a tie")
        elif computer_option == "Paper":
            print("Achka,you loose,sorry")
            computer_points = computer_points + 1
            achkata_points = achkata_points
        elif computer_option == "Scissors":
            print("Congrats Achka,you win")
            computer_points = computer_points
            achkata_points = achkata_points + 1
    if player_option == "Paper":
        if computer_option == "Rock":
            print("Congrats Achka,you win")
            computer_points = computer_points
            achkata_points = achkata_points + 1
        elif computer_option == "Paper":
            print("It is a tie")
        elif computer_option == "Scissors":
            print("Achka,you loose,sorry")
            computer_points = computer_points + 1
            achkata_points = achkata_points
    if player_option == "Scissors":
        if computer_option == "Rock":
            print("Achka,you loose,sorry")
            computer_points = computer_points + 1
            achkata_points = achkata_points
        elif computer_option == "Paper":
            print("Congrats Achka,you win")
            computer_points = computer_points
            achkata_points = achkata_points + 1
        elif computer_option == "Scissors":
            print("It is a tie")
    if player_option != "Rock" and player_option != "Paper" and player_option != "Scissors":
        print("Invalid input,try again")

    print()
    print(f"Computer points: {computer_points}")
    print(f"Achkata points: {achkata_points}")

    if computer_points == 3:
        print("Game over.The computer won the game")
        break
    elif achkata_points == 3:
        print("Game over.Achkata won the game")
        break
