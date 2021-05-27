total = 0
numbers = []

max = int(input("Enter the number of inputs to add\n >"))

try:
    for i in range(1,max+1):
        flag = 1
        while(flag):
            x = int(input("Enter a number in the range 1-5:\n"))
            if x>0 and x<6:
                total+=x
                numbers.append(x)
                flag=0
            else:
                print("Out of range")
except ValueError:
    print(ValueError)
    print("wrong input")

print("The numbers,{}\n".format(numbers))
print("The sum,{}\n".format(total))
