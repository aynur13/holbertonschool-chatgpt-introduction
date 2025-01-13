#!/usr/bin/python3

import sys

def factorial(n):
    result = 1

    while n > 1:
        result *= n
        n -= 1
    return result

# Ensure the script is called with a valid argument

if len(sys.argv) >1:
    try:
        num = int(sys.argv[1])
        if num <0:
            print("Factorial is not defined for negative numbers.")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Usage: ./script_name.py <number>")
