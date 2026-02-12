class BankAccount:
    bname = "IDBI"
    name = "AKSHAYA"
    account = 1234
    location = "NALGONDA"
    minimum_balance = 100

    def __init__(self, balance, age):
        self.balance = balance
        self.age = age

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if self.balance >= amount:
            if self.balance - amount < self.minimum_balance:
                print("Insufficient Balance")
                return
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount

    def display_details(self):
        print("Details of the customer: ")
        print(" Customer Name: ", self.name)
        print("Customer Age: ", self.age)
        print("Bank: ", self.bname)
        print("Account_Number:  ", self.account)
        print("Customer Location: ", self.location)
        print("balance amount ", self.balance)

    @classmethod
    def update_minimum_balance(cls, new_minimum_balance):
        if(new_minimum_balance < 0):
            print("Invalid")
            return
        cls.minimum_balance = new_minimum_balance

c1 = BankAccount(10000,21)
c1.display_details()
c1.withdraw(int(input("withdraw amt")))
c1.display_details()
c1.withdraw(int(input("enter withdraw amt")))
c1.withdraw(int(input("enter withdraw amt")))
c1.withdraw(int(input("enter withdraw amt")))
c1.withdraw(int(input("enter withdraw amt")))
c1.display_details()
c1.deposit(int(input("enter deposit amt")))
c1.deposit(int(input("enter deposit amt")))
c1.display_details()
BankAccount.update_minimum_balance(int(input("enter updating min bank_amt")))
c1.withdraw(int(input("enter withdraw amt")))
print(c1.balance)