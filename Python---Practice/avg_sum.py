#Program that accepts random number of inputs not greater than 10

inputs_no = 0
total = 0
avg = 0

while 1:
    x = eval(input("Enter a number\n"))

    if(inputs_no<=9):
        total+=x
        inputs_no+=1
        if(input("Are you done? y/n\n")=="y"):
            break
        
    else:
        print("Limit supposed to be not greater than 10\n")
        break

    
print("{} sum \n {} average ".format(total,total/inputs_no))
    
    
    
    
    
    
