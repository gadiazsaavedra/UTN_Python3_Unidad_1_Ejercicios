"""
Calculates the area of a circle given the radius.

Parameters:
    radio (float): The radius of the circle. Obtained via user input.
Returns:
    None: Prints out the calculated area instead of returning.

Functionality:
    1. Prompts the user to input the radius.
    2. Converts the input to a float.
    3. Validates that the radius is greater than 0.
    4. Calculates the area using the formula:
        area = pi * radius^2
    5. Prints the area formatted to 2 decimal places.
    6. Loops continuously until valid input is entered.
    7. Handles ValueError exception if input is not a number.
"""

# This is a program to calculate the area of a circle
import math

# Read the radius from the user
while True:
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius > 0:
            break
        else:
            print("Radius must be a number greater than 0")
    except ValueError:
        print("Radius must be a number")

# Compute the area of the circle
area = math.pi * radius**2

# Display the result
print(f"The area is {area:.2f}")
