def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return dividend / divisor

def get_user(user_id):
  users = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
  for user in users:
    if user["id"] == user_id:
      return user
  return None