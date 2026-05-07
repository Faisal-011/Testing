def calculate_discount(price, discount):
	if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
		raise ValueError("Price and discount must be numeric")
	return price * (1 - discount / 100)

def parse_config(config):
	if config is None:
		raise ValueError("Config cannot be None")
	return config