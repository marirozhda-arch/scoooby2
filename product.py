from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class Product:
    icon: str
    best_before_date: date
    name: str
    category: int
    price: int
    rating: float
    amount: int
    id: int | None = None
