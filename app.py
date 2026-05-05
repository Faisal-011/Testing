def divide(a, b):
  if b == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return a / b

def get_user(users, user_id):
  for user in users:
    if user['id'] == user_id:
      return user
  return None