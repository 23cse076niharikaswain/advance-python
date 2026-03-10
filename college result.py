students = {}

def add_marks():
    name = input("Enter student name: ")
    
    n = int(input("Enter number of subjects: "))
    marks = []

    for i in range(n):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    avg = sum(marks) / len(marks)
    gpa = avg / 10

    students[name] = {"marks": marks, "GPA": round(gpa, 2)}

    print("Marks added successfully!")

def show_results():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Results ---")
        for s in students:
            print("Name:", s)
            print("Marks:", students[s]["marks"])
            print("GPA:", students[s]["GPA"])
            print()

while True:
    print("\n--- College Result Management ---")
    print("1. Add Student Marks")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_marks()
    elif choice == "2":
        show_results()
    elif choice == "3":
        print("Exiting system")
        break
    else:
        print("Invalid choice")
