# Question2
# A program to calculate the volume of a sphere.
import math

# Ask the user to input the radius and convert the input to a floating-point number.
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere using the formula (4/3) * pi * r^3.
volume = (4/3) * math.pi * (radius ** 3)

# Print the calculated volume to the user.
print(f"The volume of the sphere is: {volume:.2f}")
