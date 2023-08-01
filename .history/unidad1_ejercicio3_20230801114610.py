""" ingresar el radio de una circunferencia y calcular el perimetro"""

PI = 3.14159
radio = float(input("Ingrese el radio de la circunferencia: "))
print(f"El perimetro es {round((2 * PI * radio),2)}")
area = round((PI * radio ** 2), 2)
print(f"El area es {area}")