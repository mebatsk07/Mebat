from dataclasses import dataclass, field
from typing import List


@dataclass
class MarketContext:

    # Market
    spot: float = 0.0

    timestamp: str = ""

    # Trend
    trend: str = ""

    regime: str = ""

    # Volatility
    atr: float = 0.0

    atr_percent: float = 0.0

    historical_volatility: float = 0.0

    # IV
    atm_iv: float = 0.0

    average_iv: float = 0.0

    weighted_iv: float = 0.0

    iv_rank: float = 0.0

    iv_percentile: float = 0.0

    iv_rv_ratio: float = 0.0

    expected_move: float = 0.0

    # OI
    put_oi: float = 0.0

    call_oi: float = 0.0

    put_volume: float = 0.0

    call_volume: float = 0.0

    pcr_oi: float = 0.0

    pcr_volume: float = 0.0

    support: float = 0.0

    resistance: float = 0.0

    # Sentiment
    bullish_score: float = 0.0

    bearish_score: float = 0.0

    confidence: float = 0.0

    direction: str = ""

    trade_allowed: bool = False

    reasons: List[str] = field(default_factory=list)

    # Time

hours_to_expiry: float = 0.0

trading_window_open: bool = False

# Trading

best_candidate_symbol: str = ""

best_candidate_score: float = 0.0

selected_option_type: str = ""

# Session

engine_cycle: int = 0

market_health: float = 0.0

# Risk

daily_risk_used: float = 0.0

available_margin: float = 0.0

# Open Position

open_positions: int = 0

# Performance

session_pnl: float = 0.0

def summary(self):

    return {

        "spot": self.spot,

        "trend": self.trend,

        "regime": self.regime,

        "direction": self.direction,

        "confidence": self.confidence,

        "iv_rv": self.iv_rv_ratio,

        "pcr": self.pcr_oi,

        "expected_move": self.expected_move,

    }