try:
    # User input (Risky code)
    num1 = int(input("Enter the first number: "))  # Might raise ValueError
    num2 = int(input("Enter the second number: ")) # Might raise ValueError
    result = num1 / num2
    print(result)

except ValueError: #to handle string typed
    print("Invalid string input. Please enter a valid integer.")
except ZeroDivisionError: #to handle divide by 0 error
    print("Cannot divide by zero.")
except Exception: # handle any error
    print("Something went wrong.")

finally:
    print("thank you")