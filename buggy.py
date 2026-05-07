def calculate_discount(price, discount_percentage):
	# Calculate the discount amount
	discount_amount = price * (discount_percentage / 100)
	# Subtract the discount amount from the price
	return price - discount_amount