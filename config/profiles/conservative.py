from .base import StrategyProfile

PROFILE = StrategyProfile(

    name="Conservative",

    premium_min=18,
    premium_max=25,

    delta_min=0.02,
    delta_max=0.04,

    iv_rv_min=1.5,

    max_open_positions=1,

    risk_per_trade_usd=10,

    entry_after_hour=23,

    min_expiry_hours=6,

    max_bid_ask_spread_pct=0.08,

    leverage=200,

    max_daily_loss_pct=0.03,

    max_account_drawdown_pct=0.05,
)