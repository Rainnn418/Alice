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
    zombie_position = -10
    goal = 30
    oldman_position = random.randint(1, 30)
    compass_position = random.randint(1, 15)
    pitfall_position = random.randint(1, 15)
    windstorm_position = random.randint(1, 15)
    compass_position2 = random.randint(16, 30)
    pitfall_position2 = random.randint(16, 30)
    windstorm_position2 = random.randint(16, 30)

    oldman_used = False

    print(bcolors.PURPLE + "Escape from the Misty Forest!" + bcolors.ENDC)
    print(bcolors.PURPLE + "You will: avoid zombies and reach the destination" + bcolors.ENDC)
    print(bcolors.PURPLE + "There is a god who can help you. In each round, the god will choose a number from 123. If you have telepathy with her, she can let you move forward." + bcolors.ENDC)
    print("=" * 60)
 
    while player_position < goal:
          computer_choice = random.choice("1,2,3")

          if player_position == oldman_position and not oldman_used:
               print("🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️ You meet an oldman, he told you that the number God would choose for the next round is", computer_choice)
               print("~" * 60)
               oldman_used = True
          elif player_position == compass_position:
               print("🧭🧭🧭🧭🧭 You found a compass! You can take 2 more steps!🧭🧭🧭🧭🧭")
               player_position += 2
               print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC)
               print("~" * 60)
          elif player_position == compass_position2:
               print("🧭🧭🧭🧭🧭 You found a compass! You can take 2 more steps!🧭🧭🧭🧭🧭")
               player_position += 2
               print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC)
               print("~" * 60)
          elif player_position == pitfall_position:
               print("⚠️⚠️⚠️⚠️⚠️ You fell into a pitfall! Move back 1 steps.⚠️⚠️⚠️⚠️⚠️")
               player_position -= 1
               print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC)
               print("~" * 60)
          elif player_position == pitfall_position2:
               print("⚠️⚠️⚠️⚠️⚠️ You fell into a pitfall! Move back 1 steps.⚠️⚠️⚠️⚠️⚠️")
               player_position -= 1
               print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC)
               print("~" * 60)
          elif player_position == windstorm_position:
               storm_effect = random.choice([-3, 3, 5])
               print(f"🌪️🌪️🌪️🌪️🌪️ A windstorm has moved you {storm_effect} steps!🌪️🌪️🌪️🌪️🌪️")
               player_position += storm_effect
               print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC)
               print("~" * 60)
          elif player_position == windstorm_position2:
               storm_effect = random.choice([-3, 3, 5])
               print(f"🌪️🌪️🌪️🌪️🌪️ A windstorm has moved you {storm_effect} steps!🌪️🌪️🌪️🌪️🌪️")
               player_position += storm_effect
               print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC)
               print("~" * 60)
          
          guess = input("What number did you guess?")
          move = random.choice([1,2,3,4,5])
     
          if guess == computer_choice:
               print(bcolors.GREEN + f"Guess it! You walked safely for {move} steps." + bcolors.ENDC)
               player_position += move
          elif guess != computer_choice:
               print(bcolors.RED + "Guess wrong. Try again" + bcolors.ENDC)
          elif guess < 1 or guess > 3:
               print("Invalid move. Please choose a number between 1 and 3.")
               continue
          
          print("Your position: " + bcolors.YELLOW + f"{player_position}" + bcolors.ENDC) 

          zombie_position += 1
          print("The zombie is " + bcolors.BLUE + f"{player_position - zombie_position}" + bcolors.ENDC + " steps away from you")
          print("-" * 60)

          if player_position - zombie_position == 0:
               print(bcolors.PURPLE + "🧟🧟🧟🧟🧟🧟🧟🧟 Zombie! You are dead. 🧟🧟🧟🧟🧟🧟🧟🧟" + bcolors.ENDC)
               break
          elif player_position >= goal:
               print(bcolors.YELLOW + "🎉🎉🎉🎉🎉🎉🎉🎉 Congratulations! You escaped from the Misty Forest! 🎉🎉🎉🎉🎉🎉🎉🎉" + bcolors.ENDC)
               break

misty_forest()