from dataclasses import dataclass, field

from models.trade import Trade


@dataclass
class Portfolio:

    starting_balance: float

    balance: float

    equity: float

    open_trades: list[Trade] = field(default_factory=list)

    closed_trades: list[Trade] = field(default_factory=list)

    peak_balance: float = 0

    max_drawdown: float = 0