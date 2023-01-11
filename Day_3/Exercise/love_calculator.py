# a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

nameA = name1.lower()
nameB = name2.lower()


t = (nameA.count("t") + nameB.count("t"))
r = (nameA.count("r") + nameB.count("r"))
u = (nameA.count("u") + nameB.count("u"))
e = (nameA.count("e") + nameB.count("e"))
result_1 = t + r + u + e

l = (nameA.count("l") + nameB.count("l"))
o = (nameA.count("o") + nameB.count("o"))
v = (nameA.count("v") + nameB.count("v"))
e = (nameA.count("e") + nameB.count("e"))
result_2 = l + o + v + e

love_score_1 = str(result_1) + str(result_2)
love_score = int(love_score_1)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


#RENDAN_TOCHUKWU
