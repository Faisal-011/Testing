def calculate_price(original_price, discount):
  if discount == 0:
    return original_price
  return original_price / (1 - discount / 100)

def parse_config(config):
  if 'settings' in config and 'timeout' in config:
    return config['settings'], config['timeout']
  else:
    raise ValueError("'settings' or 'timeout' key does not exist in config")