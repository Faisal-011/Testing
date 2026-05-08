def calculate_discounted_price(price, discount):
	if discount < 0:
		raise ValueError("Discount cannot be negative")
	if price <= 0:
		raise ValueError("Price must be a positive number")
	if discount == 0:
		return price
	return price - (price * discount / 100)
