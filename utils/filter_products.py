def filter_products(inventory, user_requirements):
    matching_products = inventory[
        (inventory["price"] <= user_requirements.max_price) &
        (inventory["weight_kg"] <= user_requirements.max_weight_kg) &
        (inventory["ram_gb"] >= user_requirements.min_ram_gb) &
        (inventory["storage_gb"] >= user_requirements.min_storage_gb) &
        (inventory["battery_hours"] >= user_requirements.min_battery_hours)
    ]

    return matching_products