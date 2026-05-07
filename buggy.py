import sqlite3

def connect_to_db():
	try:
		conn = sqlite3.connect('database.db')
		return conn
	except sqlite3.Error as e:
		print(f"Error connecting to database: {e}")
		return None

def validate_input(username):
	if not username:
		return False
	if not username.isalnum():
		return False
	return True

def execute_query(conn, username):
	if not validate_input(username):
		return None
	try:
		cursor = conn.cursor()
		query = "SELECT * FROM users WHERE username = ?"
		cursor.execute(query, (username,))
		results = cursor.fetchall()
		return results
	except sqlite3.Error as e:
		print(f"Error executing query: {e}")
		return None