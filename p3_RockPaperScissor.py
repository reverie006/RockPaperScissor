# Rock paper Scissor
import random
import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def computer():
    clearConsole()
    player1 = input("PLayer1 Enter your Choice: Rock(r) Paper(p) Scissor(s): \n")
    outcomes = ["r", "p", "s"]
    computerPlayer = random.choice(outcomes)
    print(f"Computer chose: \n{computerPlayer} ")
    
    if (player1.lower() == "r" and computerPlayer.lower() == "p") or (player1.lower() == "p" and computerPlayer.lower() == "r"):
        print("Rock vs Paper:\n-----Paper wins!!-----")

    elif (player1.lower() == "r" and computerPlayer.lower() == "s") or (player1.lower() == "s" and computerPlayer.lower() == "r"):
        print("Rock vs Scissor:\n-----Rock wins!!-----")

    elif (player1.lower() == "p" and computerPlayer.lower() == "s") or (player1.lower() == "s" and computerPlayer.lower() == "p"):
        print("Paper vs Scissor:\n-----Scissor wins!!-----")

    elif player1.lower() == computerPlayer.lower():
        print("-----Draw-----")

    else:
        print("-----Invalid input-----")


def manualPlayer():
    clearConsole()
    player1 = input("PLayer1 Enter your Choice: Rock(r) Paper(p) Scissor(s): \n")
    player2 = input("PLayer2 Enter your Choice: Rock(r) Paper(p) Scissor(s): \n")

    if (player1.lower() == "r" and player2.lower() == "p") or (player1.lower() == "p" and player2.lower() == "r"):
        print("Rock vs Paper:\n-----Paper wins!!-----")

    elif (player1.lower() == "r" and player2.lower() == "s") or (player1.lower() == "s" and player2.lower() == "r"):
        print("Rock vs Scissor:\n-----Rock wins!!-----")

    elif (player1.lower() == "p" and player2.lower() == "s") or (player1.lower() == "s" and player2.lower() == "p"):
        print("Paper vs Scissor:\n-----Scissor wins!!-----")

    elif player1.lower() == player2.lower():
        print("-----Draw-----")

    else:
        print("-----Invalid input-----")



userChoice = input("Wanna play with computer? (y/n): ")
while True:
    if userChoice.lower() == "y":
        computer()
    elif userChoice.lower() == "n":
        manualPlayer()
    else:
        print("Invalid input. Please choose 'y' or 'n'.")
        continue

    playAgain = input("Do you want to play again? (y/n): ")
    if playAgain.lower() != "y":
        print("Thanks for playing!")
        break