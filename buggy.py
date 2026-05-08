def calculate_price(price, discount):
  if discount > 100:
    raise ValueError("Discount cannot be greater than 100")
  return price - (price * discount / 100)