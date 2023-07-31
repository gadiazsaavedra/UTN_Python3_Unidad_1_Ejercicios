"""
Takes 3 integer values as input and calculates a result.

Parameters:
    first_input (int): The first input value
    second_input (int): The second input value
    third_input (int): The third input value

Returns:
    result (int): The calculated result

Functionality:
    1. Prompts the user to input 3 space-separated integer values
    2. Splits the input into 3 variables (first_input, second_input, third_input) 
    3. Converts the input values into integers using map()
    4. Multiplies first_input and second_input
    5. Sums third_input to the previous result 
    6. Prints the final result
"""


first_input, second_input, third_input = map(
    int, input("Ingresar 3 valores separados por espacios: ").split()
)

result = first_input * second_input + third_input
print(f"El resultado es {result}")
