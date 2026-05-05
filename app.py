def calculate(a, b):
  if b == 0:
    raise ZeroDivisionError('Cannot divide by zero')
  result = a / b
  return result

def check_user(user, id):
  if user['id'] == id:
    return True
  return False