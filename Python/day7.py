#inheritance
class vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}\nModel: {self.model}")

class car(vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

c1 = car("Toyota", "Corolla", "Red")
c1.display_info()

#Assignment
class  bankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = bankAccount(name, initial_balance)

while True:
    print("1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        case '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        case '3':
            account.display_balance()

        case '4':
            print("Exiting...")
            break

        case _:
            print("Invalid choice")

            