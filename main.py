import random, sys

print("Welcome to Rock Paper Scissors game!")
print("............. Have Fun Playing ...........")

print('''Rock, Paper, Scissors Rules:,
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

### Set up variables
Possible_actions = ['R', 'P', 'S']
CPU_wins = 0
PlayerWins = 0
ties = 0


def CPU_option():
    computerMove = random.choice(Possible_actions)
    if computerMove == 'R':
        print('R')
        computerMove ='R'
    elif computerMove == "P":
        print('P')
        computerMove ='P'   
    elif computerMove == "S":
        print('S')
        computerMove ='S'
    
while True:
    playerMove = input("What is your choice? Pick a hand ('R', 'P', 'S' or Q) '>'")
    if playerMove == 'Q':
        print('Thanks for playing!')
        sys.exit()
    elif playerMove == 'R':
        playerMove ='R'
    elif playerMove == 'P':
        playerMove ='P'
    elif playerMove == 'S':
        playerMove ='S' 
    else:
        print("I do not understand! You picked the wrong option. Type one of R, P, S, or Q. :)") 

    computerMove = random.choice(Possible_actions)
    print(f"\n Player Move {playerMove} : CPU Move {computerMove}. \n")

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print(f"Both players selected {playerMove}. It\'s a tie! Play again")
        PlayerWins = PlayerWins + 0
        CPU_wins = CPU_wins + 0
    elif playerMove == 'R' and computerMove == 'S':
        print('Congrats, You win! :)')
        PlayerWins = PlayerWins + 1
    elif playerMove == 'P' and computerMove == 'R':
        print('Congrats, You win! :)')
        PlayerWins = PlayerWins + 1
    elif playerMove == 'S' and computerMove == 'P':
        print('Congrats, You win!:)')
        PlayerWins = PlayerWins + 1
    elif playerMove == 'R' and computerMove == 'P':
        print('Sorry, You lost! :(')
        CPU_wins = CPU_wins + 1
    elif playerMove == 'P' and computerMove == 'S':
        print('Sorry, You lost! :(')
        CPU_wins = CPU_wins + 1
    elif playerMove == 'S' and computerMove == 'R':
        print('Sorry, You lost! :(')
        CPU_wins = CPU_wins + 1

    print("")
    print("Player wins: " + str(PlayerWins))
    print("Computer wins: " + str(CPU_wins))
    print("")

    playermove= input("Do you want to play again? (y/n)")
    if playermove in ["Y", "y", "yes", "Yes"]:
        pass
    elif playermove in ["N", "n", "no", "No"]:
        print("Game over! Thank you for playing :)")
        sys.exit()
