""" ingresar el radio de una circunferencia y calcular el perimetro"""

PI = 3.14159  # Assign the value of pi directly
radio = float(input("Ingrese el radio de la circunferencia: "))
print(
    "El perimetro es", (round(2 * radio * PI), 2)
)  # Print the result without rounding
