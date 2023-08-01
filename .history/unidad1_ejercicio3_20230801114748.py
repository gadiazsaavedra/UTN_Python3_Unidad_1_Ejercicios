""" ingresar el radio de una circunferencia y calcular el perimetro"""

import math

radius = float(input("Ingrese el radio de la circunferencia: "))
perimeter = 2 * math.pi * radius
print(f"El perimetro es {perimeter}")

area = math.pi * radius**2
print(f"El area es {area}")
