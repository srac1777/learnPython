def student_standing_generator():
  student_standings = ['Freshman', 'Senior', 'Junior', 'Freshman']
  # Write your code below:
  for s in student_standings:
    if s == "Freshman":
      yield 500


standing_values = student_standing_generator()
print(next(standing_values))
print(next(standing_values))
print(next(standing_values))
print(next(standing_values))
next(standing_values)
