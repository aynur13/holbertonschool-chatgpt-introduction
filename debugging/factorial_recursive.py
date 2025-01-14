#!/usr/bin/python3
import sys

# Function description:
# Calculates the factorial of a given number recursively.

# Parameters:
# n (int): The number for which factorial needs to be calculated.

# Returns:
# int: The factorial of the given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Obtains the factorial of the number provided as a command-line argument.
f = factorial(int(sys.argv[1]))
print(f)
