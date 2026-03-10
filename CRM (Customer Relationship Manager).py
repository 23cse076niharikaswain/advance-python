customers = []

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    customers.append([name, email, phone, []])

    print("Customer added")

def add_communication():
    name = input("Enter customer name: ")
    message = input("Enter communication note: ")

    for c in customers:
        if c[0] == name:
            c[3].append(message)
            print("Communication saved")
            return

    print("Customer not found")

def show_customers():
    for c in customers:
        print("Name: " + c[0])
        print("Email: " + c[1])
        print("Phone: " + c[2])

        print("Communications:")
        for m in c[3]:
            print("- " + m)

        print()

while True:
    print("\n1 Add Customer")
    print("2 Add Communication")
    print("3 Show Customers")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_customer()

    elif choice == "2":
        add_communication()

    elif choice == "3":
        show_customers()

    elif choice == "4":
        break
