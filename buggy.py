import json

class User:
	pass

def find_user(user_id):
	# Implement the find_user function with proper logic and error handling
	try:
		# Sample implementation, replace with actual database or storage logic
		users = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
		for user in users:
			if user["id"] == user_id:
				return user
	except Exception as e:
		return None

def calculate_discount(price, discount_percentage):
	# Fix the bug in the calculate_discount function
	if discount_percentage < 0 or discount_percentage > 100:
		raise ValueError("Discount percentage must be between 0 and 100")
	return price * (1 - discount_percentage / 100)

def parse_config(config_str):
	# Improve the parse_config function
	try:
		config = json.loads(config_str)
		return config
	except json.JSONDecodeError as e:
		return {}