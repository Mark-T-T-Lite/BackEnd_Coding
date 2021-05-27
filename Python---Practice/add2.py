"""
Program that lets the user input as many numbers as possible then gives
    the sum
By Mark_T
"""
total = 0

print("Program that lets the user input as many numbers "
                      "as possible then gives the sum")
while 1:
   
    try:
        x = int(input("Enter a number: "))
        if(str(type(x))=="<class 'int'>"):
            print('You have entered ',x)
        total+=x
        
    except ValueError:      #invoked_wn_user_does_not_give_integer
        print("Wrong data type.Please input an integer")
        continue
        
    if(input("Are you done? y/n ")=='y'):   #interactive, user chooses to stop inputing
        break

print("The sum of all your input numbers is {}".format(total))


'''
You can use:
    if(str(type(x))=="<class 'int'>")
'''
    
