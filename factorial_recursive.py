#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number 'n' using recursion.

# Parameters:
# n (int): The number for which the factorial is to be calculated. The function 
#         will recursively compute the product of all positive integers up to 'n'.

# Returns:
# int: The factorial of the given number 'n'. If 'n' is 0, it returns 1.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))

print(f)
