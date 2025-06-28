# First of all, we will be importing the required modules :)
import random
import string

# Function to collect user choices
def collect_user_choice():
    # using the try-except block:
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:  # Handling the value error
        print("Please enter a valid number :(")
        return None

    use_lowercase = input("Do you want to include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Do you want to include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'

    # If the input is not from any of the above:
    if not any([use_lowercase, use_uppercase, use_digits, use_symbols]):
        print("Please select at least one character type.")
        return None

    return {
        "length": length,
        "lower": use_lowercase,
        "upper": use_uppercase,
        "digits": use_digits,
        "symbols": use_symbols
    }

# Function to create the password based on settings
def create_password(settings):
    # Creating a random password based on settings of the user
    characters = ""
    if settings["lower"]:
        characters += string.ascii_lowercase
    if settings["upper"]:
        characters += string.ascii_uppercase
    if settings["digits"]:
        characters += string.digits
    if settings["symbols"]:
        characters += string.punctuation

    if not characters:
        return None

    # Generating the password by taking an empty string initially
    password = ''.join(random.choice(characters) for _ in range(settings["length"]))
    return password

# Creating the function which will be used to run the password generator
def run_generator():
    print("Your Random Password Generator ")
    settings = collect_user_choice()
    if settings:
        password = create_password(settings)
        print(f"\n Generated Password: {password}")

#For the program entry point,that is callingthe function
if __name__ == "__main__":
    run_generator()

