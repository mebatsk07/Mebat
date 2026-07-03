from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trade:

    symbol: str

    side: str

    entry_time: datetime

    exit_time: datetime | None = None

    entry_price: float = 0

    exit_price: float = 0

    quantity: int = 0

    stop_loss: float = 0

    take_profit: float = 0

    pnl: float = 0

    max_profit: float = 0

    max_loss: float = 0

    theta_captured: float = 0

    result: str = ""