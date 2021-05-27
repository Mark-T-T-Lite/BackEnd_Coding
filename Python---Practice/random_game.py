'''
    Program to generate	a random number	between	1 and 8	and ask	the user to guess the generated	number.
    Lets the user know if their	guess is correct or incorrect
'''

import random

while True:
    try:
        number = random.randint(2,7)
        x = int(input("Guess  the randomly generated number between 1 and 8:\n"))
        if x == number:
            print("Right! You got me")
               
        else:
            print("Nope. try again")


    except ValueError:
        print('Nope, try an integer; nothin else')                  
                  
