def calculate_discount(price, discount):
	if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
		raise ValueError("Price and discount must be numeric")
	return price * (1 - discount / 100)

def find_user(username, users):
	if username in users:
		return users[username]
	else:
		return None