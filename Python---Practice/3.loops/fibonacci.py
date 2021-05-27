x=0
y=1
sum=0
print("The fibonacci sequence:")
print(x)
print(y)

while(sum<10000):
    sum=x+y
    print(sum)
    x=y
    y=sum
