def get_recipe_price(prices, optionals=None, **ingredients):
    """

    :param prices:
    :param optionals:
    :param ingredients:
    :return:
    """
    # If optionals is not provided, consider all ingredients optional
    if optionals is None:
        optionals = []

    # Calculate the total price for all required ingredients (excluding optionals)
    total_price = 0
    for ingredient, quantity in ingredients.items():
        if ingredient in optionals:
            continue
        try:
            ingredient_price = prices[ingredient]
        except KeyError:
            raise KeyError(f"No price found for ingredient {ingredient}")
        price_for_quantity = ingredient_price * quantity / 100
        total_price += price_for_quantity

    return int(total_price)


# test get_recipe_price():
print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

print(get_recipe_price({}))
