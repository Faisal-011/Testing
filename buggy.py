{"def calculate_discount(price, discount_percentage):
    """Calculate the discount amount.

    Args:
    price (float): The original price.
    discount_percentage (float): The discount percentage.

    Returns:
    float: The discount amount.
    """
    discount_amount = (price * discount_percentage) / 100
    return discount_amount

# Example usage:
price = 100.0
discount_percentage = 20.0
discount_amount = calculate_discount(price, discount_percentage)
print(f"Discount amount: {discount_amount}")"}