def calculate_discount(price, discount):
  if discount == 0:
    return 0
  return price / discount

def find_user(users, username):
  for user in users:
    if user['username'] == username:
      return user
  return None