def calculate_price(original_price, discount):
	if discount < 0:
		raise ValueError("Discount cannot be negative")
	if original_price == 0:
		raise ValueError("Original price cannot be zero")
	price = original_price - (original_price * discount / 100)
	return price