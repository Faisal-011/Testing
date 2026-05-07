def find_user(users, user_id):
	if user_id not in users:
		raise ValueError("User not found")
	return users[user_id]

def calculate_discount(price, discount_percentage):
	if price < 0 or discount_percentage < 0:
		raise ValueError("Price and discount percentage must be non-negative")
	return price * discount_percentage / 100

def parse_config(config):
	try:
		# parse config logic here
	except FileNotFoundError as e:
		raise ValueError("Config file not found") from e
	except Exception as e:
		raise ValueError("Failed to parse config") from e