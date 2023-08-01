""" ingresar el radio de una circunferencia y calcular el perimetro"""

# This program calculates the perimeter and area of a circle using the radius of the circle.
import math

radius = float(input("Enter the radius of the circle: "))

perimeter = 2 * math.pi * radius

print(f"The perimeter is {perimeter}")

area = math.pi * radius**2

print(f"The area is {area}")

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
