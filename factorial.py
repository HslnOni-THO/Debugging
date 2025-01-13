#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  
    return result

f = factorial(int(sys.argv[1]))  # je prend ici l'argument de la ligne de commande
print(f)
