class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print("Withdrawal successful.")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = int(input("Enter account number: "))
        if acc_no in self.accounts:
            print("Account already exists.")
            return

        name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))

        self.accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account created successfully.")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def deposit(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)
        if not account:
            print("Account not found.")
            return

        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    def withdraw(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)
        if not account:
            print("Account not found.")
            return

        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    def transfer(self):
        from_acc = int(input("Enter sender account number: "))
        to_acc = int(input("Enter receiver account number: "))
        amount = float(input("Enter transfer amount: "))

        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if not sender or not receiver:
            print("Invalid account number.")
            return

        if sender.balance < amount:
            print("Insufficient balance.")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)
        print("Transfer successful.")

    def check_balance(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)
        if not account:
            print("Account not found.")
            return

        print(f"Current balance: {account.get_balance():.2f}")


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit()
        elif choice == "3":
            bank.withdraw()
        elif choice == "4":
            bank.transfer()
        elif choice == "5":
            bank.check_balance()
        elif choice == "6":
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
