import random
game = True
class bcolors:
     RED = '\033[91m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     BLUE = '\033[94m'
     PURPLE = '\033[95m'
     ENDC = '\033[0m'
def misty_forest():
    player_position = 0
    zombie_position = -15
    goal = 30
    torch_position = random.choice([2,25])
    compass_position = random.choice([5,25])
    pitfall_position = random.choice([5,29])
    windstorm_position = random.choice([5,29])

    print("Escape from the Misty Forest!")
    print("You will: avoid zombies and reach the destination")
    print("Be sure not to take more than 3 steps at a time!!!")
    print("=" * 60)

    while player_position < goal:
          computer_choice = random.choice([1,2,3])

          if player_position == torch_position:
               print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 You found a torch! Next turn, the safe range is", computer_choice)
               print("~" * 60)
          elif player_position == compass_position:
               print("🧭🧭🧭🧭🧭 You found a compass! You can take 2 more steps!🧭🧭🧭🧭🧭")
               player_position += 2
               print(f"Your position: {player_position}")
               print("~" * 60)
          elif player_position == pitfall_position:
               print("⚠️⚠️⚠️⚠️⚠️ You fell into a pitfall! Move back 1 steps.⚠️⚠️⚠️⚠️⚠️")
               player_position -= 1
               print(f"Your position: {player_position}")
               print("~" * 60)
          elif player_position == windstorm_position:
               storm_effect = random.choice([-3, 3, 5])
               print(f"🌪️🌪️🌪️🌪️🌪️ A windstorm has moved you {storm_effect} steps!🌪️🌪️🌪️🌪️🌪️")
               player_position += storm_effect
               print(f"Your position: {player_position}")
               print("~" * 60)
              
          move = int(input("How many steps are you going to take?"))
          
          if move == computer_choice:
               print(bcolors.GREEN + f"You walked safely for {move} steps." + bcolors.ENDC)
               player_position += move
          else:
               print(bcolors.RED + "You have been detained. Try again" + bcolors.ENDC)

          if move < 1 or move > 3:
               print("Invalid move. Please choose a number between 1 and 3.")
               continue

          print(f"Your position: {player_position}") 

          zombie_position += 1
          print("The zombie is " + bcolors.YELLOW + f"{player_position - zombie_position}"+ bcolors.ENDC + " steps away from you")
          print("-" * 60)

          if player_position - zombie_position == 0:
               print(bcolors.PURPLE + "🧟🧟🧟🧟🧟🧟🧟🧟Zombie! You are dead.🧟🧟🧟🧟🧟🧟🧟🧟" + bcolors.ENDC)
               break
          elif player_position >= goal:
               print(bcolors.BLUE + "🎉🎉🎉🎉🎉🎉🎉🎉 Congratulations! You escaped from the Misty Forest!🎉🎉🎉🎉🎉🎉🎉🎉" + bcolors.ENDC)
               break

misty_forest()