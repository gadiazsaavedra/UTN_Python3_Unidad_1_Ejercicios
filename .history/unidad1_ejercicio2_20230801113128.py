"""Incorporar el modulo sys e introduccion de parametros
luego indicar cuales son multiplos de 2"""

# The code is importing the `sys` module, which provides access to some
# variables used or maintained
# by the interpreter and to functions that interact with the interpreter.

# This code filters the even numbers from a list of numbers
# and prints the even numbers

import sys

# Filter the even numbers
even_numbers = []
for arg in sys.argv[1:]:
    try:
        num = int(arg)
        if num % 2 == 0:
            even_numbers.append(num)
    except ValueError:
        print(f"{arg} is not a valid integer")

# Print the even numbers
for num in even_numbers:
    print(f"{num} is an even number")
