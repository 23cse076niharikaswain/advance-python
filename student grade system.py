students = {}

while True:
    print("\n1.Add Grade\n2.Update Grade\n3.Delete Student\n4.Show All\n5.Exit")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Enter Student ID: ")
            if sid == "":
                raise Exception("Student ID cannot be empty")

            grade = int(input("Enter Grade: "))
            students[sid] = grade
            print("Grade added successfully")

        elif choice == "2":
            sid = input("Enter Student ID to update: ")
            if sid not in students:
                raise Exception("Invalid Student ID")

            grade = int(input("Enter new grade: "))
            students[sid] = grade
            print("Grade updated")

        elif choice == "3":
            sid = input("Enter Student ID to delete: ")
            if sid not in students:
                raise Exception("Invalid Student ID")

            del students[sid]
            print("Student removed")

        elif choice == "4":
            print(students)

        elif choice == "5":
            break

    except ValueError:
        print("Grade must be a number")
    except Exception as e:
        print("Error:", e)
