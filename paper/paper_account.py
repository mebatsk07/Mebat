from dataclasses import dataclass


@dataclass
class PaperAccount:

    starting_balance: float = 100000

    cash: float = 100000

    margin_used: float = 0

    unrealized_pnl: float = 0

    realized_pnl: float = 0

    daily_pnl: float = 0

    open_positions: int = 0

    trades_today: int = 0