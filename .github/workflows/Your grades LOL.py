average = float(input("Enter grade: "))
grade = ""

if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif average > 70:
    grade = "C"
elif average > 60:
    grade = "D"
else:
    grade = "F"
print("Your average is", average, "your grade is", grade)
