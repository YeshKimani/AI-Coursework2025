# Question3
# A program that uses functions to calculate the area and perimeter of a square.

def calculate_square_properties(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter

try:
    side_length = float(input("Enter the side length of the square: "))
    if side_length <= 0:
        print("Please enter a positive number for the side length.")
    else:
        area, perimeter = calculate_square_properties(side_length)
        print(f"The area of the square is: {area}")
        print(f"The perimeter of the square is: {perimeter}")
except ValueError:
    print("Invalid input. Please enter a numerical value.")
