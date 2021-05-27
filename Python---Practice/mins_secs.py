#Prog for mins and Secs


def mins_secs(seconds):
    mins = x//60
    secs = x%60
    print("{} seconds = {} mins {} secs".format(x,mins,secs))
    
x = eval(input("Enter The number of seconds\n"))
mins_secs(x)


