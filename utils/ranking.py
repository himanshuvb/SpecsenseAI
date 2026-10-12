def rank_products(matching_products, user_preferences):
    if matching_products.empty:
        return matching_products.copy()

    ranked_products = matching_products.copy()

    if user_preferences.get("lightweight", False):
        min_weight = ranked_products["weight_kg"].min()
        max_weight = ranked_products["weight_kg"].max()

        if max_weight == min_weight:
            ranked_products["weight_score"] = 100
        else:
            ranked_products["weight_score"] = (
                (max_weight - ranked_products["weight_kg"])
                / (max_weight - min_weight)
            ) * 100

    return ranked_products