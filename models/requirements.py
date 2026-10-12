from pydantic import BaseModel


class UserRequirements(BaseModel):
    # Hard constraints
    max_price: int | None = None
    max_weight_kg: float | None = None
    min_ram_gb: int | None = None
    min_storage_gb: int | None = None
    min_battery_hours: int | None = None

    # Soft preferences
    lightweight: bool = False
    good_battery: bool = False
    use_case: str | None = None


    # Preference priorities
    weight_priority: float = 0.0
    battery_priority: float = 0.0