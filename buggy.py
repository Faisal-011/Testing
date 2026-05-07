def find_user(users, user_id):
  if users is None or len(users) == 0:
    return None
  for user in users:
    if user['id'] == user_id:
      return user
  return None
def calculate_discount(price, discount_percentage):
  return price * (1 - discount_percentage / 100)
def parse_config(config):
  # Add config parsing logic here
  pass