# List to store student records [name, marks]
students = []

# Function to determine letter grade based on marks
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Function to add a student
def add_student(name, marks):
    students.append([name, marks])
    print("Student added successfully")

# Function to display all students with their marks and grades
def display_students():
    if len(students) == 0:
        print("No students in the gradebook")
    else:
        print("Student Gradebook:")
        for student in students:
            grade = get_grade(student[1])
            print("Name:", student[0], "Marks:", student[1], "Grade:", grade)

# Function to calculate average marks
def average_marks():
    if len(students) == 0:
        print("No students to calculate average")
    else:
        total = 0
        for student in students:
            total = total + student[1]
        avg = total / len(students)
        print("Average marks are:", avg)

# Main program
while True:
    print("\nStudent Gradebook Menu")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Average Marks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)
    elif choice == "2":
        display_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        print("Exiting gradebook")
        break
    else:
        print("Invalid choice")
