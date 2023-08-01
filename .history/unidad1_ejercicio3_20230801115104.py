""" ingresar el radio de una circunferencia y calcular el perimetro"""

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

