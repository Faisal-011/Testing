def calculate_discount(price, discount):
  if discount == 0:
    return 0
  return price / discount

def parse_config(config):
  if 'key' in config:
    return config['key']
  else:
    return None