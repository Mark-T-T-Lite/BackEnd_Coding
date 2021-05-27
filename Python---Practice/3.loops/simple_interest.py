#Simple Interest Calc

balance=2250
interestRate=0.045
term=120
month_no=1

month_int=(balance*interestRate)/12
    
while(month_no<=term):
    balance=balance+month_int
    print("Month ",month_no,"\t","interest ",month_int,"\t","Balance ",balance)
    month_no+=1
    

