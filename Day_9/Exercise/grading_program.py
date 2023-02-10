student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for grades in student_scores:
  for grades in student_scores:
  score = student_scores[grades]
  if score > 90:
    score = "Outstanding"
    student_grades[grades] = score
  elif score > 80:
    score = "Exceeds Expectation"
    student_grades[grades] = score
  elif score > 70:
    score = "Acceptable"
    student_grades[grades] = score
  elif score < 60:
    score = "fail"
    student_grades[grades] = score

print(student_grades)
