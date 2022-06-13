import random
print("Let's play Rock Paper Scissors \n"
"choose R for rock \n"
"choose P for paper \n"
"choose S for scissors \n")


#player=input("what do you choose: ")
#player = player.upper

while True: 
     game_options=["R","S","P"]
     cpu = random.choice(game_options)
     player=input("what do you choose: ")
     player = player.upper()
     print("You:",player) 
     print("CPU:",cpu) 
     
     if (player not in game_options):
     
      print("incorrect input, try again")
      continue
     elif player == cpu:
           print("it's a tie")
           print("Play again")
           player=input("what do you choose: ")
           cpu = random.choice(game_options)
           
           continue
          
     elif player=="R":
          if cpu == "S":
               print(" Rock breaks scissors,You win")
          if cpu == "P":
               print("paper covers rock, you lose") 
     elif player=="S":
          if cpu == "P":
               print(" Scissors cuts paper,You win")
          if cpu == "R":
               print("rock breaks scissors, you lose") 
     elif player=="P":
          if cpu == "S":
               print(" Scissors cuts paper,You lose")
          if cpu == "R":
               print("paper covers rock, you win")
     play_again = input("Play again? (yes/no): ").lower()

     if play_again != "yes":
        break 
               
                    
