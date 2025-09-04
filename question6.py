# Question6
values = []
sum_of_values = 0

print("Please enter 5 values to populate the list:")
for i in range(5):
    user_input = float(input(f"Enter value #{i + 1}: "))
    values.append(user_input)
    sum_of_values += user_input

average = sum_of_values / 5

print(f"\nThe values entered are: {values}")
print(f"The average of the values is: {average}")
