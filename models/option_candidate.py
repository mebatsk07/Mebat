from dataclasses import dataclass


@dataclass
class OptionCandidate:

    # Basic Information
    symbol: str
    product_id: int

    option_type: str

    strike: float

    expiry: str

    # Prices
    premium: float

    bid: float

    ask: float

    spot: float

    # Greeks
    delta: float

    gamma: float

    theta: float

    vega: float

    iv: float

    # Liquidity
    volume: float

    open_interest: float

    # Strategy Scores
    liquidity_score: float = 0

    delta_score: float = 0

    theta_score: float = 0

    premium_score: float = 0

    trend_score: float = 0

    volatility_score: float = 0

    risk_score: float = 0

    final_score: float = 0

    # Flags

    trade_allowed: bool = False

    rejection_reason: str = ""