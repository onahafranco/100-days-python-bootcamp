# check out the official game website to understand the rule of the game: https://wrpsa.com/the-official-rules-of-rock-paper-scissors

import random

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

player_choice = input(int("Type in 0 for rock, 1 for paper or 2 for scissors: "))
comp_choice = random.randint(0, 2)
if player_choice == 0 and comp_choice == 1:
  print(rock + "\ncomputer chose:" + paper + "\n You Win!")
elif player_choice == 1 and comp_choice == 0:
  print(paper + "\ncomputer chose:" + rock + "\n Computer Wins!")
elif player_choice == 0 and comp_choice == 2:
  print(rock + "\ncomputer chose:" + scissors + "\n Computer Wins!")
elif player_choice == 2 and comp_choice == 0:
  print(scissors + "\ncomputer chose:" + rock + "\n You Win!")
elif player_choice == 1 and comp_choice == 2:
  print(paper + "\ncomputer chose:" + scissors + "\n Computer Wins!")
elif player_choice == 2 and comp_choice == 1:
  print(scissors + "\ncomputer chose:" + paper + "\n You Win!")
if player_choice == comp_choice:
  print("its a draw")
else:
  print("A invalid choice")

