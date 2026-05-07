def calculate_discount(price, discount):
	if discount == 0:
		raise ValueError("Discount cannot be zero")
	return (price * discount) / 100