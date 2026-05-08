def calculate_price(original_price):
	# Input validation
	if original_price < 0:
		raise ValueError("Price cannot be negative")
	# Calculation logic
	return original_price * 1.1