def calculate_discount(price, discount_percentage):
  if discount_percentage < 0 or discount_percentage > 100:
    raise ValueError("Discount percentage must be between 0 and 100")
  return price * (1 - discount_percentage / 100)

def find_user(user_id):
  # Re-added the find_user function
  pass

def parse_config(config_file):
  # Re-added the parse_config function
  pass