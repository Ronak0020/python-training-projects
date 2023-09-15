class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def withdraw(self, amount):
        if amount > self.amount:
            print("You do not have enough money in your account!")
        else:
            self.amount -= amount
            print(f"You have successfully withdrawn: {amount} rupees.")

    def deposit(self, amount):
        self.amount += amount
        print(f"You have successfully deposited: {amount} rupees.")

    def balance(self):
        print(f"Hello, {self.name}!\nYou currently have: {self.amount} rupees.")

    def display(self):
        print(f"\n======== Welcome to XYZ bank, {self.name} ========\n\nWhat would you like to do?\n[1] Check balance\n[2] Withdraw Money\n[3] Deposit Money\n[4] Exit\n\nEnter your reply: ")
        
account = Bank("Ronak", 1500)

while True:
    account.display()
    REPLY = int(input())
    if REPLY == 1:
        account.balance()
        input("\nPress enter to continue...")
    elif REPLY == 2:
        amount = int(input("Enter the amount you wish to withdraw: "))
        account.withdraw(amount)
        input("\nPress enter to continue...")
    elif REPLY == 3:
        amount = int(input("Enter the amount you wish to deposit: "))
        account.deposit(amount)
        input("\nPress enter to continue...")
    elif REPLY == 4:
        exit()