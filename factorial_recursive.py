#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:  # Properly indented
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
