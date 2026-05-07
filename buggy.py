def calculate_disc(price, discount):
	if discount == 0:
		raise ValueError("Discount cannot be zero")
	return price * (1 - discount / 100)


def parse_config(config):
	if 'settings' not in config or 'timeout' not in config:
		raise KeyError("'settings' or 'timeout' key is missing in config")
	return config['settings'], config['timeout']