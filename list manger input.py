tasks = []

def add_task():
    name = input("Enter task name: ")
    category = input("Enter category (College/Personal/Work): ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "name": name,
        "category": category,
        "deadline": deadline,
        "priority": priority
    }

    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nAll Tasks:")
        for t in tasks:
            print(t)

def filter_by_category():
    cat = input("Enter category to filter: ")
    print("\nFiltered Tasks:")
    found = False
    for t in tasks:
        if t["category"].lower() == cat.lower():
            print(t)
            found = True

    if not found:
        print("No tasks found in this category.")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Filter by Category")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        filter_by_category()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice")
