def calculate_discount(original_price, discount_rate):
	# Input validation
	if not isinstance(original_price, (int, float)) or not isinstance(discount_rate, (int, float)):
		raise ValueError("Invalid input type")
	# Calculate discount
	return original_price * discount_rate / 100