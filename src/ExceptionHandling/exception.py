# Custom Exception Class
class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative"):
        self.message = message
        super().__init__(self.message)

try:
    # User input (Risky code)
    num1 = int(input("Enter the first number: "))  # Might raise ValueError
    num2 = int(input("Enter the second number: ")) # Might raise ValueError

    # Raise custom exception if the numbers are negative
    if num1 < 0 or num2 < 0:
        raise NegativeNumberError("Custom Error: Negative numbers are not allowed")

    # Division (Risky code)
    result = num1 / num2  # Might raise ZeroDivisionError

except ValueError:
    # Handles non-integer input (like 'abc')
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    # Handles division by zero
    print("You cannot divide by zero.")

except NegativeNumberError as e:
    # Handles negative number input
    print(e)

except Exception as e:
    # Catches all other unexpected errors
    print(f"An unexpected error occurred: {e}")

else:
    # Executes only if no exceptions occurred
    print(f"The result of the division is: {result}")

finally:
    # Always executes, whether or not an exception occurs
    print("End of program. Thanks for using the calculator!")