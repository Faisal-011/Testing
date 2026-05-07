def find_user(username, users):
	if not isinstance(username, str) or not username.strip():
		raise ValueError("Invalid username")
	if not isinstance(users, dict):
		raise ValueError("Invalid users dictionary")
	-sanitized_users = {key: value for key, value in users.items() if isinstance(key, str) and isinstance(value, dict)}
	return sanitized_users.get(username, None)

def calculate_discount(price, discount_percentage):
	if not isinstance(price, (int, float)) or not isinstance(discount_percentage, (int, float)):
		raise ValueError("Invalid input type")
	if price < 0 or discount_percentage < 0:
		raise ValueError("Invalid input value")
	return price * (1 - discount_percentage / 100)