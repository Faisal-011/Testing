def calculate_discount(price, discount):
    """
    Calculate the discount amount.

    Args:
        price (float): The original price.
        discount (float): The discount percentage.

    Returns:
        float: The discount amount.

    Raises:
        ValueError: If the discount is not within the valid range (0-100).
    """
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be within the valid range (0-100)")
    return price * (1 - discount / 100)
