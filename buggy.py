def calculate_discount(price, discount_percentage):
    """
    Calculate the discount amount based on the given price and discount percentage.

    Args:
        price (float): The original price of the item.
        discount_percentage (float): The discount percentage to apply.

    Returns:
        float: The discount amount.
    """
    return price * (discount_percentage / 100)
