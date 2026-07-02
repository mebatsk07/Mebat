from strategy.volatility import VolatilityEngine
from strategy.trend import TrendEngine


class MarketRegime:

    def __init__(self):
        self.trend = TrendEngine()
        self.volatility = VolatilityEngine()

    def detect(self, df):

        trend = self.trend.detect(df)

        vol = self.volatility.analyze(df)

        atr_percent = vol["atr_percent"]

        if trend == "UP":

            if atr_percent < 0.10:
                return "STRONG_UPTREND"

            return "VOLATILE_UPTREND"

        elif trend == "DOWN":

            if atr_percent < 0.10:
                return "STRONG_DOWNTREND"

            return "PANIC_SELLING"

        else:

            if atr_percent < 0.08:
                return "SIDEWAYS"

            return "VOLATILE_RANGE"