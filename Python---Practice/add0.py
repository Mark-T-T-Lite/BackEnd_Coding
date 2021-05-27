#Function to add any number of inputs in range of 1-5
print("Enter the number of inputs to add\n")
a=int(input(">"))
no=1 
sum_=0
while(no<=a):
    print("Enter Input ",no,"\n")
    input_=int(input(">"))
    if(input_<1 or input_>5):
        print("Limit exceeded")
        continue
    sum_+=input_
    no+=1
    
print(sum_)    
    
