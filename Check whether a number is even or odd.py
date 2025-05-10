# Function to check even or odd
def check_even_odd():
    try:
        # Input from the user
        number = int(input("Enter a number: "))

        # Check if the number is even or odd
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

# Call the function
check_even_odd()