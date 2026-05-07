def get_user():
  # using comparison operator (==) instead of assignment operator (=)
  user = "default"
  if user == "default":
    return user

def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Division by zero")
  return dividend / divisor

def check_condition():
  # simplification opportunity
  return True