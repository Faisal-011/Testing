def disco(price, discount):
	if discount == 0:
		raise ValueError("Discount cannot be zero")
	return price - (price * discount / 100)

user = {'id': 1, 'name': 'John'}
if user['id'] == 1:
	print("User found")