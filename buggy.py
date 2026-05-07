def calculate_discount(price, discount):
	if discount == 0:
		raise ValueError("Discount cannot be zero")
	return price * (1 - discount / 100)

def find_user(users, username):
	for user in users:
		if user['username'] == username:
			return user
	return None