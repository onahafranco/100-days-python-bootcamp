#a program that allows you to mark a square on the map using a two-digit system,  The first digit in the input will specify the column (the position on the horizontal axis), The second digit in the input will specify the row number (the position on the vertical axis)

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


if position == "11":
  row1[0] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "12":
  row2[0] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "13":
  row3[0] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "21":
  row1[1] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "22":
  row2[1] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "23":
  row2[1] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "31":
  row1[2] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "32":
  row2[2] = "X"
  print(f"{row1}\n{row2}\n{row3}")
elif position == "33":
  row3[2] = "X"
  print(f"{row1}\n{row2}\n{row3}")
else:
  print("wrong input! please type in a correct value")

