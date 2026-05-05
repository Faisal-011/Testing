def divide(a, b):
	try:
		if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
			raise TypeError("Both inputs must be numbers")
		if b == 0:
			raise ZeroDivisionError("Cannot divide by zero")
		return a / b
	except TypeError as e:
		return str(e)
	except ZeroDivisionError as e:
		return str(e)
	except Exception as e:
		return "An unknown error occurred: " + str(e)