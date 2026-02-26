accounts = []

def find_account(pin):
    for account in accounts:
        if account[0] == pin:
            return account
    return None

def check_balance(account):
    print("Your current balance is:", account[1])

def deposit(account, amount):
    account[1] = account[1] + amount
    print("Deposit successful. New balance is:", account[1])

def withdraw(account, amount):
    if amount > account[1]:
        print("Insufficient balance")
    else:
        account[1] = account[1] - amount
        print("Withdrawal successful. New balance is:", account[1])

def create_account():
    pin = int(input("Set a 4-digit PIN for your account: "))
    initial_balance = int(input("Enter initial balance: "))
    accounts.append([pin, initial_balance])
    print("Account created successfully")

def atm_system():
    pin = int(input("Enter your PIN: "))
    account = find_account(pin)
    if account:
        while True:
            print("\nATM Menu")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                check_balance(account)
            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                deposit(account, amount)
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: "))
                withdraw(account, amount)
            elif choice == "4":
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid PIN or account not found")

while True:
    print("\nATM Main Menu")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        atm_system()
    elif choice == "3":
        print("Exiting ATM program")
        break
    else:
        print("Invalid choice")
