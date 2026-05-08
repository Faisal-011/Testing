def disco(price, discount):
  if discount == 0:
    return "Error: Division by zero"
  return price / discount

def find_user(users, username):
  for user in users:
    if user == username:
      return user
  return None