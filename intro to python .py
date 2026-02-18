# GRADE SYSTEM PROGRAM

# Accept 5 marks
marks = []
for i in range(5):
  while True:
    try:
      mark = float(input(f"Enter mark {i+1}: "))
      marks.append(mark)
      break
    except ValueError:
      print("Invalid input! Enter a number.")

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 80:
  grade = "A"
elif average >= 60:
  grade = "B"
elif average >= 40:
  grade = "C"
else:
  grade = "D (Fail)"

# Print results
print(f"\nAverage: {average:.2f}")
print(f"Grade: {grade}")