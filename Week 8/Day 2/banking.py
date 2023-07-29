"""
bank
    new object create(constructer)
        amount=0
        account_no=randomly
        name=input
        bank_name

    withdraw
    deposit
    display
    dispalybalance
    update

obj

"""
import random


class Bank:
    """This class is used to create a bank object with some functions"""

    def __init__(self):
        self.amount = 0
        self.accno = random.randint(100000, 999999)
        self.name = input("Enter your name = ")
        self.bankName = input("Enter your bank name = ")

    def __str__(self):
        return "You have printed an object directly"

    def display(self):
        print(f"\n-------INFO-------")
        print(f"Account number = {self.accno}")
        print(f"Balance = {self.amount}")
        print(f"Name = {self.name}")
        print(f"Bank name = {self.bankName}")

    def displayBalance(self):
        """This is used to display all balance"""
        print(f"Your balance = {self.amount}")

    def deposit(self):
        """This method is used to deposit money in bank account"""
        newAmount = int(input("Enter amount to deposit = "))
        self.amount = self.amount + newAmount
        self.displayBalance()

    def withdraw(self):
        newAmount = int(input("Enter amount to withdraw = "))
        if newAmount > self.amount:
            print(f"Insufficient balance. Your actual balance is {self.amount}")
        else:
            self.amount = self.amount - newAmount
            self.displayBalance()

    def update(self):
        newName = input("Enter new name. Or if you want default leave blank = ")
        if newName != "":
            self.name = newName
        newBankName = input(
            "Enter new bank name. Or if you want default leave blank = "
        )
        if newBankName != "":
            self.bankName = newBankName


# obj = Bank()
# print(obj)
# print(obj.name)
# print(obj.amount)


# accounts = []
# accounts.append(Bank())
# accounts[0].display()

accounts = []


def searchAccount(accountNumber):
    for i in accounts:
        if i.accno == accountNumber:
            return i
        else:
            return None


while True:
    print("1.add an account")
    print("2.print all accounts")
    print("3.search account")
    print("4.deposit")
    print("5.withdraw")
    print("6.check balance")
    print("7.transfer")
    print("8.exit")
    choice = int(input("enter your choice = "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        print(f"account added.your acc number = {obj.accno}")
    elif choice == 2:
        if len(accounts) == 0:
            print("no accounts found")
        else:
            for i in accounts:
                i.display()
    elif choice == 3:
        acc_no = int(input("enter account number ="))
        for i in accounts:
            if i.accno == acc_no:
                i.display()
                break
            else:
                print("no account found")
    elif choice == 4:
        acc_no = int(input("enter account number ="))
        for i in accounts:
            if i.accno == acc_no:
                i.deposit()
                break
            else:
                print("no account found")
    elif choice == 5:
        acc_no = int(input("enter account number ="))
        for i in accounts:
            if i.accno == acc_no:
                i.withdraw()
                break
            else:
                print("no account found")
    elif choice == 6:
        acc_no = int(input("enter account number ="))
        result = searchAccount(acc_no)
        if result != None:
            result.displayBalance()
        else:
            print("no acccont found")

    elif choice == 7:
        accNo = int(input("enter your account number ="))
        senderAccount = searchAccount(acc_no)
        if senderAccount != None:
            rec_acc_no = int(input("enter receiver acc number="))
            reciverAccount = searchAccount(rec_acc_no)
            if reciverAccount != None:
                transferAmount = int(input("enter amount to tranfer= "))
                if transferAmount > senderAccount.amount:
                    print("insufficient balance")
                else:
                    reciverAccount.amount += transferAmount
                    senderAccount.amount -= transferAmount
                    print(f"your balance is {senderAccount.amount}")
            else:
                print("receiver account number is invalid")
        else:
            print("your account does not exists")
