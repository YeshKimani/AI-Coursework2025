# Question1
# A program to convert a number of days into seconds.

# Ask the user to input the number of days and convert the input to an integer.
days = int(input("Enter the number of days: "))

# Calculate the number of seconds.
# There are 24 hours in a day, 60 minutes in an hour, and 60 seconds in a minute.
seconds = days * 24 * 60 * 60

# Print the result to the user.
print(f"There are {seconds} seconds in {days} days.")
