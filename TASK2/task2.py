# BMI(Body Mass Index) calculator in Python 
#Task2
#defining a function named as "BMI_Calculation" which takes weight and height a parameters
def BMI_Calculation(weight, height):
    """We will calculate BMI using the formula: weight / (height ^ 2)"""
    bmi = weight / (height ** 2)
    return bmi
#Now we will create a funtion to check for the category with respect to the BMI 
#We will be using conditional statements(if/elif/else)
def category_WRT_BMI(bmi):
    print("This tool will help you understand your Body Mass Index.\n")
    if bmi < 18.5:
        return "You are underweight :()"
    elif 18.5 <= bmi < 25:
        return "You are normal weight :) "
    elif 25 <= bmi < 30:
        return "You are overweight :()"
    else:
        return "You are obese. Take care of your health :()"
#Defining main function
def start_calc():
    print("=== BMI Calculator ===")
#using the try-except block as it is fundamental construct for handling exceptions
    try:
        # Getting input from user :)
        #using float data type
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Validate input :)
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers . Please check input :().")
            return

        # Calculate BMI and category
        #taking 2 variables - bmi and category to call functions and store value
        bmi = BMI_Calculation(weight, height)
        category = category_WRT_BMI(bmi)

        # Displaying the final result :)
        print("\n Your BMI Summary:")
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values only :().")
#Now we will use 2 lines of code(as seen below) so that it will tell python to only run the function "start_calc() if this script is being run directly -not if it’s being imported by another script.
if __name__ == "__main__":
    start_calc()
#THIS WAS ALL FOR THE COMMAND LINE BMI CALCULATOR :)