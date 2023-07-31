"""Programa que toma tres valores por consola, luego multiplica
el 1ro por el 2do y suma el 3ro. Presenta el resultado en la terminal."""

first_input, second_input, third_input = map(
    int, input("Ingresar 3 valores separados por espacios: ").split()
)

result = first_input * second_input + third_input
print(f"El resultado es {result}")
