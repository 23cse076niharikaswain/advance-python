import base64

passwords = {}

def add_password():
    site = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    encoded = base64.b64encode(password.encode())

    passwords[site] = [username, encoded]

    print("Password saved successfully")

def view_password():
    site = input("Enter website name: ")

    if site in passwords:
        username = passwords[site][0]
        encoded = passwords[site][1]

        decoded = base64.b64decode(encoded).decode()

        print("Username: " + username)
        print("Password: " + decoded)
    else:
        print("Website not found")

while True:
    print("\n1 Add Password")
    print("2 View Password")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_password()

    elif choice == "3":
        break
