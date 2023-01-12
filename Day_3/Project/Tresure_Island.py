# Treasure Island by Onaha Brendan Tochukwu

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
||  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

name = input("what is your name?: ")
print(f"welcome on board {name} brace up!! you are in for a bumpy ride!!")
direction = input("what direction will you want to turn to, left or right?: ")
direction = direction.lower()
if direction == "right":
    print("Sorry you fell into a ditch \n Game over!")
elif direction == "left":
  action = input("will you prefer to swim or ride a horse? ")
  action = action.lower()
  if action == "swim":
    print("You were attacked and killed by a Shark\nGame Over!")
  elif action == "ride a horse":
    house = input("which house will you love to stop by, The Castle, The Cottage or the Hut?: ").lower()
    if house == "the castle":
      print("You have been attacked and killed by the casle beast\nGame Over!")
    elif house == "the cottage":
      print("You were shot and killed by the old man who owns the cottage\n Game Over")
    elif house == "the hut":
      print("Congratulations! you found the treasure box, you are rich!!\nYou Win!!!")
    else:
      print("Game over")
  else:
    print("invalid input\nGame over!")
else:
  print("invalid input\nGame over")
