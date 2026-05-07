def calculate_discount(price, discount):
  if discount == 0:
    return price
  else:
    return price - (price * discount / 100)

def find_user(user_id):
  # implement user finding logic here
  pass

def parse_config(config):
  try:
    # config parsing logic here
    pass
  except Exception as e:
    # proper error handling mechanism
    print(f"Error parsing config: {e}")