import random

print("Welcome to Rock Paper Scissors game!")
print("............. Have Fun Playing ...........")

### Set up variables
CPUScore = 0
PlayerScore = 0
TieScore = 0
PossibleHands = ['R' == "Rock", 'P' == "Paper", 'S' == "Scissors"]

def checkForWinner(player_choice, CPU_choice):
  if(player_choice == "Rock" and CPU_choice == "Paper"):
    print("Player (Rock) : CPU (Paper)")
    print("Sorry you lost :(")
    return "Cpu"
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
    return "Cpu"
  elif(player_choice == "Paper" and CPU_choice == "Rock"):
    print("Player (Paper) : CPU (Rock)")
    print("Congrats! You win :)")
    return "Player"
  elif(player_choice == "Paper" and CPU_choice == "Scissors"):
    print("Player (Paper) : CPU (Scissors)")
    print("Sorry, you lost!")
    return "Cpu"
  else:
    print("It's a tie, play again!")
    return "Tie"

### Start game loop
while(PlayerScore != 3 and CPUScore != 3):

  ### Validate input
  while True:
    def choose_option(player_choice):
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
  
    ### Generate computer pick
    CPU_choice = random.choice(PossibleHands)
    
    ### Print results
    print("Player: ", player_choice,)
    print("CPU: ", CPU_choice)
    result = checkForWinner(player_choice, CPU_choice)
    if(result == "Player"):
      PlayerScore += 1
    elif(result == "CPU"):
      CPUScore += 1
    else:
      TieScore += 1
    print("Your score: ", PlayerScore, "CPU: ", CPUScore, "Ties: ", TieScore)

print("Game over! Thank you for playing :)")
