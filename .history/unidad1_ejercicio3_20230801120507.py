""" ingresar el radio de una circunferencia y calcular el perimetro"""

# This code is calculating the perimeter and area of a circumference based
# on the radius entered by
# the user. It uses the math module to access the value of pi and
# perform mathematical calculations.
# The code prompts the user to enter the radius, calculates the perimeter using the formula 2 * π *
# radius, and prints the result. Then, it calculates the area using the formula π * radius^2 and
# prints the result.

import math

# Prompt the user to enter the radius of the circumference
radius = float(input("Ingrese el radio de la circunferencia: "))

# Calculate the perimeter of the circumference using
# the formula: 2 * π * radius
perimeter = 2 * math.pi * radius

# Print the calculated perimeter
print(f"El perimetro es {perimeter}")

# Calculate the area of the circumference using the formula: π * radius^2
area = math.pi * radius**2

# Print the calculated area
print(f"El area es {area}")
