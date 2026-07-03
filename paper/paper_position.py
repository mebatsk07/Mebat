from dataclasses import dataclass
from datetime import datetime


@dataclass
class PaperPosition:

    symbol: str

    side: str

    quantity: int

    entry_price: float

    current_price: float

    stop_loss: float

    target: float

    entry_time: datetime

    expiry: datetime

    pnl: float = 0

    status: str = "OPEN"