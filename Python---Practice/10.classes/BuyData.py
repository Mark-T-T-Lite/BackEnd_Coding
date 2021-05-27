""" 
solution to QUESTION 1

Name: KALANZI JUDE
Reg NO: 18/U/23550/PS
COURSE: BSTE 

"""

import random

class Bank_Account:

    def __init__(self):
        self.account_number = 0
        self.balance = 0
        self.charge = 2000
        self.name = "unregistered"

    def generateAccountNumber(self):
        if (self.balance < 10000):
            print("insufficient funds")
        else :
            print("which transaction do you want to make ?")
            
           
    def generateAccountNumber(self):
        range_start = 10**(9)
        range_end = (10**10)-1
        num = random.randrange(range_start, range_end)
        self.account_number = num
        print(num)
    
    def createAccount(self,firstName,SecondName):
        self.name = firstName + " " + SecondName
        while self.balance < 10000:
            self.balance = eval(input("Minimum Balance for an account is 10,000\n Enter your deposit"))
            if self.balance >= 10000:
                self.generateAccountNumber()
                print("account successfully created:\n Account Name: "+self.name+"\n Account Number: ", self.account_number,"\n Account Balance: ",self.balance,"\n" )
            else:
                print("Minimum required")

    def deposit(self):
        amount= int(input("Enter amount to be Deposited: "))
        self.balance += amount
        self.balance -= self.charge
        print("\n Amount Deposited: ",amount,"\n Service fee: ", self.charge,"\n Current Balance: ", self.balance)
  
    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            self.balance -= self.charge
            print("\n You Withdrew:", amount,"\n Service fee: ", self.charge,"\n Current Balance: ", self.balance)
        else:
            print("\n Insufficient balance  ")

    def transferMoney(self,accountTo,amount):        
        if self.balance < (amount+self.charge):
            print("you've inssufficient funds")
            return
        else:
            # dedducting charges
            self.balance-=(amount+self.charge)

            print ("Successfully transfered ",amount," to Account number ",5010505551 if accountTo == 1 else 1029427421) 
            print("Charge: 2000\n the new balance is ",amount)
            return

# testing
print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
while 1:

    choice = eval(input("\nPlease chooSe an option below:\n1.Open an account\n2.withdraw money\n3.deposit money\n4.transfer money\n"))
    if choice == 1:
        account1 = Bank_Account()
        account1.createAccount(input("Your First name"),input("your last name"))

    elif choice == 2:
        account1.withdraw()

    elif choice == 3:
        account1.deposit()

    elif choice == 4:
        receipient=int(input("Contact list:\n 1.5010505551\n2.1029427421\n Choose receipient\n"))
        transferAmount= int(input("Enter amount to transfer\n"))
        if receipient <= 2 and receipient > 0:
            account1.transferMoney(receipient,transferAmount)
        else:
            print("unknown receipient")

    else:  
        break


