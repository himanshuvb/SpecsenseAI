def normalize_score(series, higher_is_better=True):
    min_value = series.min()
    max_value = series.max()

    if min_value == max_value:
        return series * 0 + 100

    if higher_is_better:
        return (series - min_value) / (max_value - min_value) * 100

    return (max_value - series) / (max_value - min_value) * 100


def rank_products(matching_products, user_preferences):
    if matching_products.empty:
        return matching_products.copy()

    ranked_products = matching_products.copy()
    weighted_scores = []
    total_priority = 0

    if user_preferences.lightweight and user_preferences.weight_priority > 0:
        ranked_products["weight_score"] = normalize_score(
            ranked_products["weight_kg"],
            higher_is_better=False
        )

        weighted_scores.append(
            ranked_products["weight_score"] * user_preferences.weight_priority
        )
        total_priority += user_preferences.weight_priority

    if user_preferences.good_battery and user_preferences.battery_priority > 0:
        ranked_products["battery_score"] = normalize_score(
            ranked_products["battery_hours"]
        )

        weighted_scores.append(
            ranked_products["battery_score"] * user_preferences.battery_priority
        )
        total_priority += user_preferences.battery_priority

    if total_priority == 0:
        return ranked_products

    ranked_products["recommendation_score"] = (
        sum(weighted_scores) / total_priority
    )

    return ranked_products.sort_values(
        by="recommendation_score",
        ascending=False
    )
