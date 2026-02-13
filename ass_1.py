class BankAccount:
    bname="IDBI"
    location="NALGONDA"
    minimum_balance=100

    def __init__(self,balance,age,name):
        self.balance=balance
        self.age=age
        self.name=name
        

    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount")
            return
        if self.balance-amount<self.minimum_balance:
            print("Insufficient Balance")
            return
        self.balance-=amount
        print("Withdrawal successful")

    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount")
            return
        self.balance+=amount
        print("Deposit successful")

    def display_details(self):
        print("Customer Name:",self.name)
        print("Customer Age:",self.age)
        print("Bank:",self.bname)
        print("Location:",self.location)
        print("Balance:",self.balance)

    @classmethod
    def update_minimum_balance(cls,new_minimum_balance):
        if new_minimum_balance<0:
            print("Invalid minimum balance")
            return
        cls.minimum_balance=new_minimum_balance
        print("Minimum balance updated")


c1=BankAccount(10000,21,"Akshaya")
c1.display_details()
c1.withdraw(int(input("Enter withdraw amount:")))
c1.display_details()
c1.deposit(int(input("Enter deposit amount:")))
c1.display_details()
BankAccount.update_minimum_balance(int(input("Enter new minimum balance:")))
c1.withdraw(int(input("Enter withdraw amount:")))
print("Final Balance:",c1.balance)
