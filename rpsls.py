from random import randint
import sys


print('Let\'s play ROCK-PAPER-SCISSORS-LIZARD-SPOCK?\nIt\'s like a regular ROCK-PAPER-SCISSORS but added with LIZARD and SPOCK.')

#input player name
player_name = input('\nPlease enter your name!\n')

#Rules
print(f'\nHello {player_name}! So here is the rules...\n\nAs Sheldon Cooper from The Big Bang Theory explains, \"Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.\" Anytime you want to quit the game, just type \'Exit\'. HAVE FUN!')

#generate choices
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#assign a random play to the computer
computer = t[randint(0,4)]

#set player to False
player = False

#assign score variables
playerScore = 0
computerScore = 0

while player == False:
#set player to True
    player = input("\nRock, Paper, Scissors, Lizard, Spock?\n")
    print(f"The computer choices {computer}")

    if player == computer:
        print("Tie!")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computerScore += 1
        elif computer == "Scissors":
            print("You win!", player, "crushes", computer)
            playerScore += 1
        elif computer == "Lizard":
            print("You win!", player, "crushes", computer)
            playerScore += 1
        elif computer == "Spock":
            print("You lose!", computer, "vaporizes", player)
            computerScore += 1

    elif player == "Paper":
        if computer == "Rock":
            print("You win!", player, "covers", computer)
            playerScore += 1
        elif computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computerScore += 1
        elif computer == "Lizard":
            print("You lose!", computer, "eats", player)
            computerScore += 1
        elif computer == "Spock":
            print("You win!", player, "disproves", computer)
            playerScore += 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computerScore += 1
        elif computer == "Paper":
            print("You win!", player, "cut", computer)
            playerScore += 1
        elif computer == "Lizard":
            print("You win!", player, "decapitates", computer)
            playerScore += 1
        elif computer == "Spock":
            print("You lose...", computer, "smashes", player)
            computerScore += 1

    elif player == "Lizard":
        if computer == "Rock":
            print("You lose...", computer, "crushes", player)
            computerScore += 1
        elif computer == "Paper":
            print("You win!", player, "eats", computer)
            playerScore += 1
        elif computer == "Scissors":
            print("You lose...", computer, "decapitates", player)
            computerScore += 1
        elif computer == "Spock":
            print("You win!", player, "poisons", computer)
            playerScore += 1

    elif player == "Spock":
        if computer == "Rock":
            print("You win!", player, "vaporizes", computer)
            playerScore += 1
        elif computer == "Paper":
            print("You lose...", computer, "disproves", player)
            computerScore += 1
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
            playerScore += 1
        elif computer == "Lizard":
            print("You lose...", computer, "poisons", player)
            computerScore += 1
#exit game
    elif player == 'Exit':
        print('Exiting program....')
        print(f'Your score : {playerScore}, Computer score: {computerScore}')
        if playerScore > computerScore:
            print(f'You win! Congratulations {player_name}, you rock!')
        else:
            print(f'Too bad. Better luck next time!')
        sys.exit()
        break

    else:
        print("That's not a valid play. Check your spelling!")

    print("Your score:", str(playerScore) + ", Computer score:", str(computerScore))

    player = False
    computer = t[randint(0,4)]