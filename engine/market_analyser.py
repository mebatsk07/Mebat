from models.market_context import MarketContext

from strategy.market_regime import MarketRegimeDetector
from strategy.trend import TrendEngine
from strategy.volatility_engine import VolatilityEngine
from strategy.oi_engine import OIEngine
from strategy.iv_engine import IVEngine
from strategy.direction_engine import DirectionEngine


class MarketAnalyzer:

    def __init__(self):

        self.regime_engine = MarketRegimeDetector()

        self.trend_engine = TrendEngine()

        self.volatility_engine = VolatilityEngine()

        self.iv_engine = IVEngine()

        self.oi_engine = OIEngine()

        self.direction_engine = DirectionEngine()

    # --------------------------------------------------
    # MAIN
    # --------------------------------------------------

    def analyze(

        self,

        candles,

        option_chain,

    ) -> MarketContext:

        context = MarketContext()

        # -----------------------------------------
        # Spot Price
        # -----------------------------------------

        context.spot = candles[-1].close

        context.timestamp = str(candles[-1].timestamp)

        # -----------------------------------------
        # Trend
        # -----------------------------------------

        context.trend = self.trend_engine.detect(candles)

        # -----------------------------------------
        # Regime
        # -----------------------------------------

        context.regime = self.regime_engine.detect(candles)

        # -----------------------------------------
        # Volatility
        # -----------------------------------------

        vol = self.volatility_engine.calculate(candles)

        context.atr = vol.atr

        context.atr_percent = vol.atr_percent

        context.historical_volatility = vol.historical_volatility

        # -----------------------------------------
        # IV
        # -----------------------------------------

        iv = self.iv_engine.calculate(

            option_chain,

            context.spot,

        )

        context.atm_iv = iv.atm_iv

        context.average_iv = iv.average_iv

        context.weighted_iv = iv.weighted_iv

        context.iv_rank = iv.iv_rank

        context.iv_percentile = iv.iv_percentile

        context.iv_rv_ratio = iv.iv_rv_ratio

        context.expected_move = iv.expected_move

        # -----------------------------------------
        # OI
        # -----------------------------------------

        oi = self.oi_engine.calculate(

            option_chain,

            context.spot,

        )

        context.put_oi = oi.put_oi

        context.call_oi = oi.call_oi

        context.put_volume = oi.put_volume

        context.call_volume = oi.call_volume

        context.pcr_oi = oi.pcr_oi

        context.pcr_volume = oi.pcr_volume

        context.support = oi.support

        context.resistance = oi.resistance

        # -----------------------------------------
        # Direction
        # -----------------------------------------

        direction = self.direction_engine.calculate(context)

        context.direction = direction.direction

        context.confidence = direction.confidence

        context.bullish_score = direction.bullish_score

        context.bearish_score = direction.bearish_score

        # -----------------------------------------
        # Trading Window
        # -----------------------------------------

        context.trade_allowed = True

        context.reasons.clear()

        return context