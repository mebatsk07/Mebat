from datetime import datetime

from strategy.trend_engine import TrendEngine
from strategy.volatility_engine import VolatilityEngine
from strategy.iv_engine import IVEngine
from strategy.oi_engine import OIEngine

from dataclasses import dataclass, field
from typing import List


# =====================================================
# MARKET CONTEXT
# =====================================================

@dataclass
class MarketContext:

    timestamp: str

    spot: float

    trend: str
    trend_strength: float

    atr: float
    atr_percent: float
    historical_volatility: float

    iv_state: str
    iv_rv_ratio: float

    pcr_oi: float
    pcr_volume: float

    direction: str
    confidence: float

    support: float
    resistance: float

    trade_allowed: bool
    reasons: List[str] = field(default_factory=list)


# =====================================================
# MARKET ANALYZER
# =====================================================

class MarketAnalyzer:

    def __init__(self):

        self.trend_engine = TrendEngine()
        self.vol_engine = VolatilityEngine()
        self.iv_engine = IVEngine()
        self.oi_engine = OIEngine()

    # -------------------------------------------------
    # INPUTS
    # -------------------------------------------------

    def get_inputs(self):

        from collectors.option_market_collector import OptionMarketCollector
        from collectors.btc_collector import BTCCollector

        btc = BTCCollector().fetch()
        market = OptionMarketCollector().fetch()

        df = btc["df"]
        tickers = market["result"]

        return df, tickers

    # -------------------------------------------------
    # MAIN ANALYSIS
    # -------------------------------------------------

    def analyze(self, df, tickers):

        # ---------------- TREND ----------------
        trend_ctx = self.trend_engine.detect(df)
        spot = float(df["close"].iloc[-1])

        # ---------------- VOLATILITY ----------------
        vol_ctx = self.vol_engine.analyze(df)

        # ---------------- IV ----------------
        iv_ctx = self.iv_engine.analyze(
            tickers=tickers,
            spot=spot,
            historical_volatility=vol_ctx["historical_volatility"],
        )

        # ---------------- OI ----------------
        oi_ctx = self.oi_engine.analyze(
            tickers=tickers,
            spot=spot,
        )

        # ---------------- FILTER ----------------
        reasons = []
        trade_allowed = True

        if vol_ctx["atr_percent"] > 10:
            trade_allowed = False
            reasons.append("High volatility")

        if iv_ctx.iv_rv_ratio < 1.0:
            trade_allowed = False
            reasons.append("Low IV environment")

        if trend_ctx == "UP" and oi_ctx.direction == "STRONG_BULLISH":
            trade_allowed = False
            reasons.append("Strong bullish pressure")

        if trend_ctx == "DOWN" and oi_ctx.direction == "STRONG_BEARISH":
            trade_allowed = False
            reasons.append("Strong bearish pressure")

        # ---------------- RETURN ----------------
        return MarketContext(

            timestamp=str(datetime.utcnow()),

            spot=spot,

            trend=trend_ctx,
            trend_strength=50,

            atr=vol_ctx["atr"],
            atr_percent=vol_ctx["atr_percent"],
            historical_volatility=vol_ctx["historical_volatility"],

            iv_state=iv_ctx.iv_state,
            iv_rv_ratio=iv_ctx.iv_rv_ratio,

            pcr_oi=oi_ctx.pcr_oi,
            pcr_volume=oi_ctx.pcr_volume,

            direction=oi_ctx.direction,
            confidence=oi_ctx.confidence,

            support=oi_ctx.strongest_support,
            resistance=oi_ctx.strongest_resistance,

            trade_allowed=trade_allowed,
            reasons=reasons,
        )