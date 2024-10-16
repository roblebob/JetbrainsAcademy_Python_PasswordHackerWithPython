# Dictionary of student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "David": 78,
    "Emma": 95
}

# Get student name from user input
student_name = input()

# Check if the student name exists in the dictionary and print their grade
# TODO: Write your code here
filtered = {k: v for k, v in student_grades.items() if k == student_name}
if filtered:
    print(filtered[student_name])
else:
    print("Not found")