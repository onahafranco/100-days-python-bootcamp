# a program that checks if it is a leap year or not


year = int(input("Which year do you want to check? "))

# how a nested loop looks like
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
