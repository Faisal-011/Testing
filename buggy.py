def calculate_price(price, discount):
	if not isinstance(price, (int, float)) or price < 0:
		raise ValueError("Price must be a non-negative number")
	if not isinstance(discount, (int, float)) or discount < 0 or discount > 100:
		raise ValueError("Discount must be between 0 and 100")
	return price - (price * discount / 100)