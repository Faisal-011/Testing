def divide(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both 'a' and 'b' must be numbers.")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    except TypeError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")