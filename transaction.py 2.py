balance = 0
transactions = []

password = input("Enter password: ")
if password != "izzel@0550":
    print("Wrong password! Program stopped.")
else:
    print("Login successful!\n")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance = balance + amount
                transactions.append("Deposited: " + str(amount))
                print("Deposit successful!")
            else:
                print("Invalid amount!")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Not enough balance!")
            elif amount <= 0:
                print("Invalid amount!")
            else:
                balance = balance - amount
                transactions.append("Withdrawn: " + str(amount))
                print("Withdrawal successful!")

        elif choice == "3":
            print("Your balance is:", balance)

        elif choice == "4":
            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                print("Transaction History:")
                for item in transactions:
                    print(item)

        elif choice == "5":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice! Try again.")
