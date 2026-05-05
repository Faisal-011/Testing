try:
	user_id = user['id']
except KeyError:
	raise ValueError("'id' key not found in user dictionary")