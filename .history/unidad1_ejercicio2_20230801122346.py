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
for argument in sys.argv[1:]:
    try:
        NUMBER = int(argument)
        if NUMBER % 2 == 0:
            even_numbers.append(NUMBER)
    except ValueError:
        print(f"{argument} is not a valid integer")

# Print the even numbers
for number in even_numbers:
    print(f"{N} is an even number")
