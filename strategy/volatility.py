import pandas as pd
import numpy as np

from strategy.indicators import atr


class VolatilityEngine:

    def analyze(self, df):

        df = df.copy()

        # ATR
        df["atr"] = atr(df)

        # Log Returns
        df["returns"] = np.log(
            df["close"] /
            df["close"].shift(1)
        )

        # Historical Volatility
        df["hv"] = (
            df["returns"]
            .rolling(30)
            .std()
            * np.sqrt(365)
        )

        latest = df.iloc[-1]

        return {

            "atr": float(latest["atr"]),

            "historical_volatility":
                float(latest["hv"]),

            "close":
                float(latest["close"]),

            "atr_percent":
                float(
                    latest["atr"] /
                    latest["close"] * 100
                )
        }