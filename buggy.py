def find_user(user_id, users):
	for user in users:
		if user['id'] == user_id:
			return user
	return None

def calculate_discount(price, discount):
	if discount == 0:
		return price
	else:
		return price - (price * discount / 100)

def parse_config(config):
	# Add error handling for config parsing
	try:
		# Config parsing logic here
		return parsed_config
	except Exception as e:
		return None