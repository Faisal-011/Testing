def calculate_discount(price, discount):
	if discount == 0:
		return 0
	else:
		return price * (1 - discount / 100)
