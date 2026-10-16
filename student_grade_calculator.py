
# Student Grade Calculator
# Created by Prakash

print("=" * 40)
print("       STUDENT GRADE CALCULATOR")
print("=" * 40)

name = input("Enter student name: ")

subjects = ["English", "Mathematics", "Computer Science", "Physics", "Chemistry"]
marks = []

for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter marks in {subject} (0-100): "))

            if 0 <= score <= 100:
                marks.append(score)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

total = sum(marks)
percentage = total / len(subjects)

if any(score < 35 for score in marks):
    result = "FAIL"
    grade = "F"
elif percentage >= 90:
    result = "PASS"
    grade = "A+"
elif percentage >= 80:
    result = "PASS"
    grade = "A"
elif percentage >= 70:
    result = "PASS"
    grade = "B"
elif percentage >= 60:
    result = "PASS"
    grade = "C"
elif percentage >= 35:
    result = "PASS"
    grade = "D"
else:
    result = "FAIL"
    grade = "F"

print("\n" + "=" * 40)
print("          STUDENT REPORT CARD")
print("=" * 40)

print("Student Name:", name)

for subject, score in zip(subjects, marks):
    print(f"{subject:<20}: {score:g}/100")

print("-" * 40)
print(f"Total Marks          : {total:g}/500")
print(f"Percentage           : {percentage:.2f}%")
print(f"Grade                : {grade}")
print(f"Result               : {result}")
print("=" * 40)
print("Thank you for using this program!")
