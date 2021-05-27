#P...

x = eval(input("Enter Any Year to check\n>"))
sum=0

for year in range(x,1601,-1):
    if (year % 100) == 0:
        if (year % 400) == 0:
            #print("{0} is a leap year".format(year))
            sum+=1
            continue
    elif (year % 4) == 0:
        sum+=1
        continue
        
print(sum)
exit()
