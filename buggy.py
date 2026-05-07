def calculate_discount(price, discount):
	if discount == 0:
		return 0
	else:
		return price * (1 - discount)

def find_user(user_id):
	# original find_user function implementation
	pass

def parse_config(config):
	try:
		# parse config logic
	pass
	except Exception as e:
		handle_error(e)
