def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return dividend / divisor

def get_user(id, users):
  for user in users:
    if user['id'] == id:
      return user
  return None