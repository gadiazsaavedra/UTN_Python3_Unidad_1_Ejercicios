"""
Takes an integer input, increments it by 10%, and prints the result.

Parameters:
    valor (int): The integer value input by the user.

Returns:
    None: Prints the result instead of returning it.

Functionality:
    1. Prompts user to input an integer value.
    2. Stores the input in the valor variable.
    3. Increments valor by 10%:
        valor_incrementado = valor + (valor * 0.1)
    4. Prints valor_incrementado using an f-string.
"""

# The code is asking the user to input an integer value and
# storing it in the variable `valor`. Then,
# it calculates the value incremented by 10% and stores it
# in the variable `valor_incrementado`.
# Finally, it prints the result using an f-string.

# Se solicita el ingreso de un valor entero
valor = int(input("Ingresar un valor entero: "))

# Se calcula el incremento del 10% del valor ingresado
valor_incrementado = valor + (valor * 0.1)

# Se redondea el resultado a dos decimales
valor_incrementado = round(valor_incrementado, 2)

# Se muestra el resultado del incremento
print(f"El valor incrementado en 10% es {valor_incrementado}")
