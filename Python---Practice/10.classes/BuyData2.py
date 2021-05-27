import time

ACCOUNTS = {'Name1':"Candice Donka",'A/C_No1':1003456222,'Amount1':10000,
            'Name2': "Angella Bittu",'A/C_No2':1002223456,'Amount2':1000000}


def transferMoney(amount):
    print("Initiating transfer\n")
    time.sleep(2)
    print("Sender: ", ACCOUNTS['Name2'], "\nAccount number: ", ACCOUNTS['A/C_No2'],"\nAccount Balance: ", ACCOUNTS['Amount2'])
    time.sleep(3)
    print("\nReceiver: ", ACCOUNTS['Name1'], "\nAccount number: ", ACCOUNTS['A/C_No1'],"\nAccount Balance: ", ACCOUNTS['Amount1'])

    print("\n\nTransfering: ", amount," to ",ACCOUNTS['Name1'])
    ACCOUNTS['Amount1'] += amount
    time.sleep(3)
    print("\n",ACCOUNTS['Name1'], " has received ", amount,"\nNew Account Balance: ", ACCOUNTS['Amount1'])


transferMoney(int(input("Enter amount to transfer\n")))