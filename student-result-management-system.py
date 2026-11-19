# Student Result Management System

print("===== STUDENT RESULT MANAGEMENT SYSTEM =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subjects = ["Python", "DBMS", "Operating System", "Computer Networks", "DSA"]

marks = []
total = 0

for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        break

    marks.append(mark)
    total += mark

else:
    percentage = total / len(subjects)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n========== STUDENT RESULT ==========")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", "PASS" if percentage >= 40 else "FAIL")
    print("====================================")
