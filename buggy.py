import sqlite3

def find_user(username):
	params = (username,)
	params_query = "SELECT * FROM users WHERE username = ?"
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute(params_query, params)
	user = cursor.fetchone()
	conn.close()
	return user