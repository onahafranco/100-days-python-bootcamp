# a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("input current age: ")
years = 90 
time_left = int(years) - int(age)
days = 365 * time_left
weeks = 52 * time_left
months = 12 * time_left

print(f"You have {days} days, {weeks} weeks, and {months} months left")
