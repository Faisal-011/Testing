{"def calculate_discount(price, discount_percentage):
    """Calculate the discount amount based on the given price and discount percentage.\n    """
    if discount_percentage > 100:\n        raise ValueError("Discount percentage cannot exceed 100%")\n    discount_amount = (price / 100) * discount_percentage\n    return discount_amount\n"}