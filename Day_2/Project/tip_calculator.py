# A program that splits tips and bills between friends..

print("Welcome to the tip calculator")

bill = input("what is the bill($)? ")
tip_percentage = input("what percetage tip will you like to give? ")

#the value of our tip will be:
tip = (float(bill) / int(100)) * float(tip_percentage)
total_bill = float(bill) + float(tip)

#lets know the nuber of persons splitting the bill
spliters = input("how many people will split the bill?: ")

#amount to go round rounded in two decimal places will be:
amount = (round(total_bill / int(spliters), 2))

print(f"each person will pay: ${amount}")
