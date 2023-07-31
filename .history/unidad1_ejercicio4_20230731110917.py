""" ingresar el radio de una circunferencia y calcular el area"""
import math

while True:
    try:
        radio = float(input("Ingrese el radio de la circunferencia: "))
        
        area = math.pi * math.pow(radio, 2)
        print(f"El area es {area:.2f}")
        break
    except ValueError:
        print("Debe ingresar un numero")
