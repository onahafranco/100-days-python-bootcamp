# import random module
import random

# Using slit function to split names
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_num = len(names)
random_number = random.randint(0, name_num - 1)
rand_name = names[random_number]
print(rand_name + " is going to buy the meal today")
