# Question4
# A program that uses a function to determine if a character is uppercase or lowercase.

def check_character_case(char):
    if 'a' <= char <= 'z':
        return "lowercase"
    elif 'A' <= char <= 'Z':
        return "uppercase"
    else:
        return "neither uppercase nor lowercase"

char_input = input("Enter a single character: ")

if len(char_input) == 1:
    result = check_character_case(char_input)
    print(f"The character '{char_input}' is {result}.")
else:
    print("Please enter only a single character.")
