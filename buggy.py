def calculate_discount(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise ValueError("Price and discount must be numeric")
    return price * (1 - discount / 100)

def find_user(user_id):
    # Implement the find_user function logic here
    pass

def parse_config(config):
    settings = config.get('settings', {})  # Provide a default value
    timeout = config.get('timeout', 60)  # Provide a default value
    return settings, timeout