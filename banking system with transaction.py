accounts = {
    "101": 5000,
    "102": 3000
}

while True:
    print("\n--- Banking System ---")
    print("1. Transfer Money")
    print("2. Show Accounts")
    print("3. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sender = input("Enter Sender Account Number: ")
            receiver = input("Enter Receiver Account Number: ")
            amount = float(input("Enter Amount: "))

            if sender not in accounts or receiver not in accounts:
                raise Exception("Incorrect account number")

            if accounts[sender] < amount:
                raise Exception("Overdraft! Insufficient balance")

            accounts[sender] -= amount
            accounts[receiver] += amount

            print("Transaction Successful")

        elif choice == "2":
            print("Account Details:")
            for acc, bal in accounts.items():
                print("Account:", acc, "Balance:", bal)

        elif choice == "3":
            print("Thank you for using the banking system")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid amount entered")
    except Exception as e:
        print("Error:", e)
