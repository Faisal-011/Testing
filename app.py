def safe_divide(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Both 'a' and 'b' must be numbers")
  if abs(b) < 1e-9:
    raise ZeroDivisionError("Cannot divide by zero")
  return a / b