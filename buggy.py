try:
	price = float(price)
	discount_percentage = float(discount_percentage)
	result = price * (1 - discount_percentage / 100)
except ValueError:
	result = None