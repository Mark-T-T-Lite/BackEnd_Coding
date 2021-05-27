import time
class LycaMobile:

    def __init__(self):
        self.duration = 24
        self.airtimeBalance = 0
        self.use= "yes"

    def buy(self,amount):
        self.airtimeBalance += amount
        return self.airtimeBalance
    
    def buyMyPakaBundle(self):
        bundle = int(input("\t\tLYCAMOBILE \n 1. 10 minutes, 5mbs, 5sms at 500 \n 2. buy 20 minutes, 10mbs, 10sms at 700 \n 3. 30 minutes, 20mbs, 20sms at 1000 "))
        check = bundle 
        if bundle == 1:
            if self.airtimeBalance < 500:
                print ("insufficient balance")
                return
            else:
                self.airtimeBalance -= 500
                self.use= input("used bundle? yes/no")
                time.sleep(2)
                if check == bundle and self.use=="no":
                    print("Time for the daily bundle has passed, but since your data is unused\n Extended for 6 hours")
                elif self.use == "yes":
                    print("Bundle Has Expired, Please recharge")
        elif bundle == 2:          
                if self.airtimeBalance < 700:
                    print ("insuffiecient balance")
                    return
                else:
                    self.airtimeBalance -= 700
                    self.use= input("used bundle? yes/no")
                    time.sleep(2)
                    if check == bundle and self.use=="no":
                        print("Time for the daily bundle has passed, but since your data is unused\n Extended for 6 hours")
                    elif self.use == "yes":
                        print("Bundle Has Expired, Please recharge")                    

        elif bundle == 3:         
                if self.airtimeBalance < 1000:
                    print ("insufficient balance")
                    return
                else:
                    self.airtimeBalance -= 1000
                    self.use= input("used bundle? no/yes")
                    time.sleep(2)
                    if check == bundle and self.use=="no":
                        print("Time for the daily bundle has passed, but since your data is unused\n Extended for 6 hours")
                    elif self.use == "yes":
                        print("Bundle Has Expired, Please recharge")
                    
        else:
            print("unknown option ")
            return

user = LycaMobile()

airtime = user.buy(int(input("\t\tLYCAMOBILE\n Buy airtime\n minimum is 500\n")))
user.buyMyPakaBundle()

           
