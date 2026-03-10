freelancers = []
clients = []
projects = []

def register_freelancer():
    name = input("Enter freelancer name: ")
    skill = input("Enter skill: ")

    freelancers.append([name, skill])

    print("Freelancer registered")

def register_client():
    name = input("Enter client name: ")
    clients.append(name)

    print("Client registered")

def assign_project():
    project = input("Enter project name: ")
    freelancer = input("Assign to freelancer: ")
    payment = input("Enter payment amount: ")

    projects.append([project, freelancer, payment])

    print("Project assigned")

def show_projects():
    for p in projects:
        print("Project: " + p[0])
        print("Freelancer: " + p[1])
        print("Payment: " + p[2])
        print()

while True:
    print("\n1 Register Freelancer")
    print("2 Register Client")
    print("3 Assign Project")
    print("4 Show Projects")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_freelancer()

    elif choice == "2":
        register_client()

    elif choice == "3":
        assign_project()

    elif choice == "4":
        show_projects()

    elif choice == "5":
        break
