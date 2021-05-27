'''
    Contains is_prime which checks for a prime number.
'''

from math import sqrt

def is_prime(n):
    """ Determines the primality of a given value.
            n an integer to test for primality.
            using root of n is a faster testing method.
        Returns true if n is prime; otherwise, returns false.
    """
    root = round(sqrt(n)) + 1 
    
    for trial_factor in range(2, root): # Try all potential factors from 2 to the square root of n
        if n % trial_factor == 0: # Is it a factor?
            return False # Found a factor
    return True # No factors found
    
def main():
    """ Tests for primality each integer from 2 up to a value provided by the user.
        If an integer is prime, it prints it; otherwise, the number is not printed.
    """
    max_value = int(input("Display primes up to what value? "))
    for value in range(2, max_value + 1):
        if is_prime(value): # See if value is prime
            print(value) # Display the prime number           
       
        
main() # Run the program
