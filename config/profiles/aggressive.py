from .base import StrategyProfile

PROFILE = StrategyProfile(

    name="Aggressive",

    premium_min=12,
    premium_max=35,

    delta_min=0.02,
    delta_max=0.08,

    iv_rv_min=1.2,

    max_open_positions=3,

    risk_per_trade_usd=20,

    entry_after_hour=23,

    min_expiry_hours=6,

    max_bid_ask_spread_pct=0.12,

    leverage=200,

    max_daily_loss_pct=0.05,

    max_account_drawdown_pct=0.07,
)