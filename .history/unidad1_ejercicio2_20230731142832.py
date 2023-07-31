"""Incorporar el modulo sys e introduccion de parametros
luego indicar cuales son multiplos de 2"""

# The code is importing the `sys` module, which provides access to some
# variables used or maintained
# by the interpreter and to functions that interact with the interpreter.

import sys

# Filter the even numbers
even_numbers = (x for x in sys.argv[1:] if int(x) % 2 == 0)

# Print the even numbers
for arg in even_numbers:
    print(f"{arg} is an even number")
