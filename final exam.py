class User:
    def __init__(self, name , user_id , password , initial_balance=0):
        self.name = name
        self.user_id = user_id
        self.password = password
        self.balance = initial_balance
        self.loan_amount = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            return True
        else:
            print("Insufficient balance. Unable to withdraw.")
            return False

    def transfer(self, amount, recipient):
        if self.withdraw(amount):
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to {recipient.user_id}")

    def check_balance(self):
        return self.balance

    def take_loan(self):
        if self.loan_amount == 0:
            loan_limit = self.balance * 2
            self.loan_amount = int(input(f"Enter loan amount (Up Till {loan_limit}): "))
            if self.loan_amount > loan_limit:
                print("Loan amount exceeds the limit.")
                self.loan_amount = 0
            else:
                self.balance += self.loan_amount
                self.transaction_history.append(f"Loan taken: {self.loan_amount}")
        else:
            print("You already have a loan.")

    def view_transaction_history(self):
        return self.transaction_history


class Admin:
    def __init__(self) :
        self.users = []

    def create_user(self, name , user_id , password , initial_balance=0):
        user = User(name, user_id , password , initial_balance)
        self.users.append(user)

    def total_bank_balance(self):
        return sum(user.balance for user in self.users)

    def total_loan_amount(self):
        return sum(user.loan_amount for user in self.users)

    def loan_feature(self, user, status):
        user.take_loan = status


def main():
    admin = Admin()

    while True:
        print("\n----- Banking Management System ----- ")
        print("1. Create an account ")
        print("2. Log in as a user ")
        print("3. Log in as an admin ")
        print("4. Exit ")

        choice = input("Enter your choice: ")

        if choice == "1" :
            name = input("Your name : ")
            user_id = input("Your user ID : ")
            password = input("Your password : ")
            initial_balance = float(input("Enter starting balance : "))
            admin.create_user(name, user_id, password, initial_balance)
            print("Account created successfully ")

        elif choice == "2":
            user_id = input("your user ID : ")
            password = input("your password : ")

            user = next((u for u in admin.users if u.user_id == user_id and u.password == password), None)
            if user:
                while True:
                    print("\n===== User Menu =====")
                    print("1. Deposite money")
                    print("2. Withdraw money")
                    print("3. available balance")
                    print("4. Transfer money")
                    print("5. transaction history")
                    print("6. Take a loan")
                    print("7. Log out")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        amount = float(input("Enter the deposite amount: "))
                        user.deposit(amount)

                    elif user_choice == "2":
                        amount = float(input("Enter the withdrawal amount: "))
                        user.withdraw(amount)

                    elif user_choice == "3":
                        print(f"Available balance: {user.check_balance()}")

                    elif user_choice == "4":
                        recipient_id = input("Enter the recipient's user ID  ")
                        recipient = next((u for u in admin.users if u.user_id == recipient_id), None)
                        if recipient:
                            amount = float(input("Enter the transfer amount : "))
                            user.transfer(amount, recipient)
                        else:
                            print("Recipient not found.")

                    elif user_choice == "5":
                        print("Transaction History:")
                        for transaction in user.view_transaction_history():
                            print(transaction)

                    elif user_choice == "6":
                        user.take_loan()

                    elif user_choice == "7":
                        print("Logged out.")
                        break

            else:
                print("Invalid user ID or password.")

        elif choice == "3":
            admin_password = input("Enter the admin password: ")
            if admin_password == "admin_password":  
                while True:
                    print("\n===== Admin Menu =====")
                    print("1. available balance")
                    print("2. loan amount")
                    print("3. loan_feature (On/Off)")
                    print("4. Log out as admin")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        print(f"Total available balance: {admin.total_bank_balance()}")

                    elif admin_choice == "2":
                        print(f"Total loan amount: {admin.total_loan_amount()}")

                    elif admin_choice == "3":
                        loan_status = input("Enter 'On' to enable loans, 'Off' to disable: ")
                        for user in admin.users:
                            admin.loan_feature(user, loan_status.lower() == "on")
                        print("Loan feature updated.")

                    elif admin_choice == "4":
                        print("Logged out as admin.")
                        break

            else:
                print("Invalid admin password.")

        elif choice == "4":
            print("Exiting the Banking Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
