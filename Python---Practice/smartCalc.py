'''
    Basic Calculator Program with add, subtract, multiply, divide
    -Interactive
    -By Mark_T
'''

def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)

def main():
    print("Basic Calculator Program with add, subtract, multiply(x), divide(/)\n"
          "-Interactive\n"
          "-By Mark_T")
    while 1:
       
        try:
            x = input("Enter your expression:\n > ")
            
            if("+" in x):
                index = x.find("+")
                print(add(int(x[0:index]),int(x[index+1:])))
                #print(x.find("+"))
            elif("-" in x):
                index = x.find("-")
                print(subtract(int(x[0:index]),int(x[index+1:])))
            elif("x" in x):
                index = x.find("x")
                print(multiply(int(x[0:index]),int(x[index+1:])))
            elif("/" in x):
                index = x.find("/")
                print(divide(int(x[0:index]),int(x[index+1:])))
                
            else:
                print("Unknown Operation. Example: 1x5")
                        
        except ValueError:
            print(ValueError.args)
            continue
            
        if(input("Are you done? y/n ")=='y'):   #interactive, user chooses to stop inputing
            break
    

main()


