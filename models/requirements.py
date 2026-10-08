from pydantic import BaseModel



class UserRequirements(BaseModel):
    max_price: int | None = None
    max_weight_kg: float | None = None
    min_ram_gb: int | None = None
    min_storage_gb: int | None = None
    min_battery_hours: int | None = None
    