import random 

print("Welcome to Rock Paper Scissors game")
print("............. Have Fun Playing ...........")

### Set up Variables
CPU_score = 0
Player_score = 0
Tie_score = 0
PossibleHands = ['R' == "Rock", 'P' == "Paper", 'S' == "Scissors"]

RPS = ['R','P','S']

def choose_option():
    player_choice = input("What is your choice? Pick a hand ('R' for Rock, 'P' for Paper, 'S' for Scissors): """)
    if player_choice in ["R"]:
        player_choice = 'R'
    elif player_choice in ["P"]:
        player_choice = 'P'
    elif player_choice in ["S"]:
        player_choice = 'S'
    else:
      print("I do not understand! You picked the wrong option. Try again. :)")
      choose_option()
      return player_choice

def computer_option(): 
CPU_choice = random.choice(PossibleHands)

def checkForWinner(player_choice, CPU_choice):
    if(player_choice == "Rock" and CPU_choice == "Paper"):
        print("Player (Rock) : CPU (Paper)")
        print("Sorry you lost :(")
        return "CPU"
    elif(player_choice == "Rock" and CPU_choice == "Scissors"):
        print("Player (Rock) : CPU (Scissors)")
        print("Congrats! You have won :)")
        return "Player"
    elif(player_choice == "Scissors" and CPU_choice == "Paper"):
        print("Player (Scissors) : CPU (Paper)")
        print("Congrats! You win :)")
        return "Player"
    elif(player_choice == "Scissors" and CPU_choice == "Rock"):
        print("Player (Scissors) : CPU (Rock)")
        print("Sorry, you lost!")
        return "CPU"
    elif(player_choice == "Paper" and CPU_choice == "Rock"):
        print("Player (Paper) : CPU (Rock)")
        print("Congrats! You win :)")
        return "Player"
    elif(player_choice == "Paper" and CPU_choice == "Scissors"):
        print("Player (Paper) : CPU (Scissors)")
        print("Sorry, you lost!")
        return "CPU"
    else:
        print("It's a tie, play again!")
        return "Tie"


while(Player_score != 3 and CPU_score != 3):
  
  while True:
    print("")
    
    player_choice = choose_option()
    CPU_choice = computer_option()

### Print results

print("Player: ", player_choice)
print("CPU: ", CPU_choice)
result = checkForWinner(player_choice, CPU_choice)
if(result == "Player"):
    Player_score += 1
elif(result == "Cpu"):
    CPU_score += 1
else:
    Tie_score += 1

print("Your score: ", Player_score, "CPU: ", CPU_score, "Ties: ", Tie_score)

player_choice = input("Do you want to play again? (y/n)")
if player_choice in ["Y", "y", "yes", "Yes"]:
    pass
elif player_choice in ["N", "n", "no", "No"]:
    print("Game over! Thank you for playing :)")

