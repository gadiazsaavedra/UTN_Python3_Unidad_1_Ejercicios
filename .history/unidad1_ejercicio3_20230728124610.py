""" ingresar el radio de una circunferencia y calcular el perimetro"""

import math

radio = float(input("Ingrese el radio de la circunferencia: "))
print(f"El perimetro es {round((2radio * math.pi),2)}")
