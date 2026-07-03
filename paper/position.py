from dataclasses import dataclass
from datetime import datetime


@dataclass
class PaperPosition:

    # --------------------------------------------------
    # Instrument
    # --------------------------------------------------

    symbol: str

    product_id: int

    side: str              # SELL

    option_type: str

    strike: float

    expiry: str

    quantity: int

    # --------------------------------------------------
    # Prices
    # --------------------------------------------------

    entry_price: float

    current_price: float

    stop_loss: float

    target_price: float

    # --------------------------------------------------
    # Greeks at Entry
    # --------------------------------------------------

    delta: float = 0.0

    theta: float = 0.0

    gamma: float = 0.0

    vega: float = 0.0

    iv: float = 0.0

    # --------------------------------------------------
    # Time
    # --------------------------------------------------

    entry_time: datetime | None = None

    exit_time: datetime | None = None

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    status: str = "OPEN"

    exit_reason: str = ""

    # --------------------------------------------------
    # Exit
    # --------------------------------------------------

    exit_price: float = 0.0

    # --------------------------------------------------
    # PnL
    # --------------------------------------------------

    realized_pnl: float = 0.0

    unrealized_pnl: float = 0.0

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    highest_profit: float = 0.0

    maximum_drawdown: float = 0.0

    theta_captured: float = 0.0

    premium_decay: float = 0.0

    trade_health: float = 100.0

    # --------------------------------------------------
    # Strategy
    # --------------------------------------------------

    trade_score: float = 0.0