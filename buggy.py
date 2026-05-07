def calculate_discount(price, discount_percentage):
	if not isinstance(price, (int, float)) or price < 0:
		raise ValueError("Price must be a non-negative number")
	if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0 or discount_percentage > 100:
		raise ValueError("Discount percentage must be between 0 and 100")
	return price * (1 - discount_percentage / 100)