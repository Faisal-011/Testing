def calculate_discount(price, discount):
	if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
		raise ValueError("Price and discount must be numbers")
	if discount < 0 or discount > 100:
		raise ValueError("Discount must be between 0 and 100")
	if discount == 0:
		return price
	return price - (price * discount / 100)
