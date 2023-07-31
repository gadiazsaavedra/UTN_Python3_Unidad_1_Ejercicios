"""calcular el area """
# This code calculates the area of a circle.
import math

while True:
    try:
        radio = float(input("Ingrese el radio de la circunferencia: "))
        if radio > 0:
            area = math.pi * radio**2
            print(f"El area es {area:.2f}")
            break
        else:
            print("Ingresar un número mayor a cero")
    except ValueError("Radius must be a number"):
        print("Debe ingresar un número")
