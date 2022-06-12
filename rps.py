from random import randint

t = ["R", "P", "S"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Welcome to Eru's game.\nSelect R for Rock, P for Paper, S for Scissors\n")
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("Player (Rock) : CPU (Paper)\nYou lose!", computer, "covers", player)
        else:
            print("Player (Rock) : CPU (Scissors)\nYou win!", player, "smashes", computer)
    elif player == "P":
        if computer == "S":
            print("Player (Paper) : CPU (Scissors)\nYou lose!", computer, "cut", player)
        else:
            print("Player (Paper) : CPU (Rock)\nYou win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Player (Scissors) : CPU (Rock)\nYou lose...", computer, "smashes", player)
        else:
            print("Player (Scissors) : CPU (Paper)\nYou win!", player, "cut", computer)
    else:
        print("Invalid input. Try again")
    player = False
    computer = t[randint(0,2)]