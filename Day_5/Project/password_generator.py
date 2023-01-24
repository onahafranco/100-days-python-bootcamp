# a program that asks for user input to determine the length of password, and then generate a randomized password of desired length for the user

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []
for sy in range(1, nr_symbols + 1):
  password = password + [random.choice(symbols)]
for num in range(1, nr_symbols + 1):
  password = password + [random.choice(numbers)]
for let in range(1, nr_symbols + 1):
  password = password + [random.choice(letters)]
random.shuffle(password)

#converting list to str
new_pass = ""
for strpass in password:
  new_pass = new_pass + strpass
print(f"your password is {new_pass}")  
