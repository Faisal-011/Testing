def calculate_discount(price, discount):
	if discount == 0:
		return price
	else:
		return price * (1 - discount)


def parse_config(config):
	try:
		# parse config code here
	except ValueError as e:
		raise ValueError("Invalid config: " + str(e))
	except TypeError as e:
		raise TypeError("Invalid config type: " + str(e))