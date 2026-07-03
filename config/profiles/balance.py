from .base import StrategyProfile

PROFILE = StrategyProfile(

    name="Balanced",

    premium_min=15,
    premium_max=30,

    delta_min=0.02,
    delta_max=0.05,

    iv_rv_min=1.3,

    max_open_positions=2,

    risk_per_trade_usd=15,

    entry_after_hour=23,

    min_expiry_hours=6,

    max_bid_ask_spread_pct=0.10,

    leverage=200,

    max_daily_loss_pct=0.03,

    max_account_drawdown_pct=0.05,
)