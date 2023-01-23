#a program that calculates the average student height from a List of heights without using the len() and sum() functions

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

Total_Height = 0
for height in student_heights:
    Total_Height += height
#print(Total_Height)

number_of_students = 0
for students in student_heights:
    number_of_students += 1
#print(number_of_students)

average_height = Total_Height / number_of_students

print(round(average_height))
