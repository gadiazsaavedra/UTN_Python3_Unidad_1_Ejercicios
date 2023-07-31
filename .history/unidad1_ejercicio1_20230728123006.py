"""Programa que toma tres valores por consola, luego multiplica
el 1ro por el 2do y suma el 3ro. Presenta el resultado en la terminal."""
VARIABLE1, VARIABLE2, VARIABLE3 = map(int, input("Ingresar 3 valores separados por espacios: ").split())
result = VARIABLE1 * VARIABLE2 + VARIABLE3
print(f"El resultado es {result}")
