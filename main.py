import random
game = True
def misty_forest():
    player_position = 0
    zombie_position = -5
    goal = 30
    torch_position = random.choice([2,35])
    compass_position = random.choice([5,35])
    pitfall_position = random.choice([10,39])
    windstorm_position = random.choice([15,39])
     
    print("Escape from the Misty Forest!")
    print("You will: avoid zombies and reach the destination")
    print("Be sure not to take more than 3 steps at a time!!!")
    print("=" * 60)

    while player_position < goal:
          computer_choice = random.choice([1,2,3])
          move = int(input("How many steps are you going to take?"))

          if move < 1 or move > 3:
               print("Invalid move. Please choose a number between 1 and 3.")
               continue

          if move == computer_choice:
               print(f"You walked safely for {move} steps.")
               player_position += move
          else:
               print("You have been detained. Try again")
        
          if player_position == torch_position:
               print("🔥 You found a torch! Next turn, the safe range is", computer_choice)
          elif player_position == compass_position:
               print("🧭 You found a compass! You can take 2 more steps!")
               player_position += 2
          elif player_position == pitfall_position:
               print("⚠️ You fell into a pitfall! Move back 3 steps.")
               player_position -= 3
          elif player_position == windstorm_position:
               storm_effect = random.choice([-3, 3, 5])
               print(f"🌪️ A windstorm has moved you {storm_effect} steps!")
               player_position += storm_effect

          print(f"Your position: {player_position}")

          zombie_position += 1
          print(f"The zombie is {player_position - zombie_position} steps away from you")
          print("-" * 60)

          if player_position - zombie_position == 0:
               print("🧟 Zombie! You are dead.")
               game = False 
              
    print("🎉 Congratulations! You escaped from the Misty Forest!")
misty_forest()