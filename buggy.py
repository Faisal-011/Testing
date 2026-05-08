def calculate_price(original_price, discount):
	if discount == 0:
		return original_price
	price_after_discount = original_price - (original_price * discount / 100)
	return price_after_discount