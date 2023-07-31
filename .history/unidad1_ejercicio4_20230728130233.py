""" ingresar el radio de una circunferencia y calcular el area"""

import math

PI = math.pi
radius = float(input("Ingrese el radio de la circunferencia: "))
area = PI * radius**2
print(f"El area es {area:.2f}")
