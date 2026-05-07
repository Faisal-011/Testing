def calculate_discount(price, discount):
	if not isinstance(discount, (int, float)) or discount < 0 or discount > 100:
		raise ValueError("Discount must be a number between 0 and 100")
	return price * (1 - discount / 100)

def find_user(users, user_id):
	for user in users:
		if user['id'] == user_id:
			return user
	return None