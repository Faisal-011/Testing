def calculate_discount(price, discount):
  if discount == 0:
    return 0
  return price / discount

def find_user(users, user_id):
  for user in users:
    if user['id'] == user_id:
      return user
  return None

def parse_config(config):
  if 'settings' in config and 'timeout' in config:
    return config['settings'], config['timeout']
  else:
    return None, None