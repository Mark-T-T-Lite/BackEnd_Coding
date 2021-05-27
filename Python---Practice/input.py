""""
This is a Quotation
"""
'''
This is a muliti
line
comment.
'''
import math
#USING INPUT()
print(input("What is your name \n ")+" is a nice name")
name = input("Name:")
age = int(input("age:"))
gpa = int(input("gpa:"))

print(name,age,gpa)
print(max(age,gpa))
print(min(age,gpa))
print(math.sqrt(age))

#FOR LOOP
for gpa in range(gpa,50,1):
    print(gpa)
