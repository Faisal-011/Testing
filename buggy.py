def calculate_discount(price, discount):
	if discount < 0 or discount > 100:
		raise ValueError("Discount must be between 0 and 100")
	return price * (1 - discount / 100)

def find_user(username):
	if not isinstance(username, str) or len(username) == 0:
		raise ValueError("Username must be a non-empty string")
	# Add additional validation and sanitization as needed
	return username