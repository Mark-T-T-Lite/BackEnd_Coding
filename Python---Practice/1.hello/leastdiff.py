def least_difference(a,b,c):
    """
Returns the difference between two of the ordered set(a,b,c)

>>> least_difference(1, 5, -5)
    4
"""
    dif1 = abs(a-b)
    dif2 = abs(b-c)
    dif3 = abs(c-a)
    return min(dif1,dif2,dif3)

print(least_difference(1,2,3) )
help(least_difference)
