from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    available: float
    hold: float
    total: float
    frozen: bool
    transactions: dict