contacts = {}

while True:
    print("\n1.Add Contact\n2.Edit Contact\n3.Search Contact\n4.Exit")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")

            if name == "" or phone == "":
                raise Exception("Fields cannot be empty")

            if name in contacts:
                raise Exception("Duplicate contact")

            if not phone.isdigit() or len(phone) != 10:
                raise Exception("Invalid phone number format")

            contacts[name] = phone
            print("Contact saved")

        elif choice == "2":
            name = input("Enter Name to edit: ")

            if name not in contacts:
                raise Exception("Contact not found")

            phone = input("Enter new phone: ")

            if not phone.isdigit():
                raise Exception("Invalid phone format")

            contacts[name] = phone
            print("Contact updated")

        elif choice == "3":
            name = input("Enter Name to search: ")

            if name not in contacts:
                raise Exception("Contact not found")

            print("Phone:", contacts[name])

        elif choice == "4":
            break

    except Exception as e:
        print("Error:", e)
