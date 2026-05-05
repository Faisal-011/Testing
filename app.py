try:
	# Check for division by zero
	if denominator == 0:
		raise ZeroDivisionError("Cannot divide by zero")
	result = numerator / denominator
except ZeroDivisionError as e:
	print(f"Error: {e}")

# Corrected comparison operator
if user_id == expected_id:
	print("User ID matches")