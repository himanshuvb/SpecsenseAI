def has_actionable_requirements(user_requirements):
    return any([
        user_requirements.max_price is not None,
        user_requirements.max_weight_kg is not None,
        user_requirements.min_ram_gb is not None,
        user_requirements.min_storage_gb is not None,
        user_requirements.min_battery_hours is not None,
        user_requirements.lightweight,
        user_requirements.good_battery,
        user_requirements.use_case is not None,
    ])
