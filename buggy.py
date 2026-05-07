def calculate_discount(price, discount):
	if discount < 0 or discount > 100:
		raise ValueError("Discount must be between 0 and 100")
	return price * (1 - discount / 100)

class Product:
	def __init__(self, price, discount=0):
		self.price = price
		self.discount = discount

	def get_price_after_discount(self):
		return calculate_discount(self.price, self.discount)
