def filter_products(inventory, user_requirements):
    '''
    Filter products based on the user's hard requirements.

    Args:
        inventory: Pandas DataFrame containing all available products.
        user_requirements: Structured requirements extracted from the user's query.

    Returns:
        Pandas DataFrame containing products that meet the hard constraints.
    '''

    filters = {
        "price": ("max_price", "<="),
        "weight_kg": ("max_weight_kg", "<="),
        "ram_gb": ("min_ram_gb", ">="),
        "storage_gb": ("min_storage_gb", ">="),
        "battery_hours": ("min_battery_hours", ">=")
    }

    matching_products = inventory.copy()

    for column, (requirement, operator) in filters.items():
        value = getattr(user_requirements, requirement)

        if value is not None:
            if operator == "<=":
                matching_products = matching_products[
                    matching_products[column] <= value
                ]
            else:
                matching_products = matching_products[
                    matching_products[column] >= value
                ]

    return matching_products