def find_user(user_id, users):
	for user in users:
		if user['id'] == user_id:
			return user
	return None