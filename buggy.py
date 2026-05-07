def calculate_discount(price, discount):
  if discount == 0:
    return price
  else:
    return price * (1 - discount)

def find_user(user_id):
  # implement find_user function
  pass

def parse_config(config):
  try:
    # parse config
    pass
  except Exception as e:
    # define handle_error function or replace with proper error handling
    print(f"Error parsing config: {e}")