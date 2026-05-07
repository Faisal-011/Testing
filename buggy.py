def calculate_discount(price, discount):
  if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
    raise ValueError("Price and discount must be numeric")
  return price * (1 - discount / 100)

def find_user(username):
  if not isinstance(username, str):
    raise ValueError("Username must be a string")
  # Add additional validation and sanitization
  username = username.strip()
  if len(username) == 0:
    raise ValueError("Username cannot be empty")
  # Example of a secure way to query a database
  # users = db.query("SELECT * FROM users WHERE username = ?", username)
  return username