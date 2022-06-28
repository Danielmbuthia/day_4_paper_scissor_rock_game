rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
computer_choice = random.randint(0,2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(player_choice)
print(computer_choice)

if player_choice >=3 or player_choice < 0:
  print("You picked a wrong choice you loss")
if computer_choice == 0:
  if player_choice == 0:
    print("You draw")
  if player_choice == 1:
    print("You win")
  if player_choice == 2:
    print("You Loss")
if computer_choice == 1:
  if player_choice == 0:
    print("You lose")
  if player_choice == 1:
    print("You draw")
  if player_choice == 2:
    print("You Win")
if computer_choice == 2:
  if player_choice == 0:
    print("You lose")
  if player_choice == 1:
    print("You lose")
  if player_choice == 2:
    print("You draw")