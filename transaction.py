from dataclasses import dataclass

@dataclass
class Transaction:
    type: str
    customer: int
    id: int
    amount: float