from dataclasses import dataclass

from strategy.indicators import (
    atr,
    atr_percent,
    historical_volatility,
    realized_volatility,
    rolling_std,
)


# =====================================================
# VOLATILITY CONTEXT
# =====================================================

@dataclass
class VolatilityContext:

    atr: float

    atr_percent: float

    historical_volatility: float

    realized_volatility: float

    rolling_std: float

    volatility_regime: str

    expansion: bool

    compression: bool

    volatility_score: float

    explanation: list[str]


# =====================================================
# VOLATILITY ENGINE
# =====================================================

class VolatilityEngine:

    def analyze(self, df):

        df = df.copy()

        # ------------------------------------
        # Calculate indicators
        # ------------------------------------

        df["atr"] = atr(df)

        df["atr_percent"] = atr_percent(df)

        df["hv"] = historical_volatility(df)

        df["rv"] = realized_volatility(df)

        df["rolling_std"] = rolling_std(df["close"])

        latest = df.iloc[-1]

        atr_value = float(latest["atr"])

        atr_pct = float(latest["atr_percent"])

        hv = float(latest["hv"])

        rv = float(latest["rv"])

        std = float(latest["rolling_std"])

        explanation = []

        # ------------------------------------
        # Regime Classification
        # ------------------------------------

        regime = "NORMAL"

        score = 50

        expansion = False

        compression = False

        if atr_pct >= 4:

            regime = "EXTREME"

            score = 100

            expansion = True

            explanation.append(
                "ATR extremely high"
            )

        elif atr_pct >= 3:

            regime = "HIGH"

            score = 80

            expansion = True

            explanation.append(
                "High ATR"
            )

        elif atr_pct >= 2:

            regime = "NORMAL"

            score = 60

            explanation.append(
                "Normal volatility"
            )

        elif atr_pct >= 1:

            regime = "LOW"

            score = 40

            compression = True

            explanation.append(
                "Low volatility"
            )

        else:

            regime = "VERY_LOW"

            score = 20

            compression = True

            explanation.append(
                "Volatility compression"
            )

        return VolatilityContext(

            atr=round(atr_value, 2),

            atr_percent=round(atr_pct, 2),

            historical_volatility=round(hv, 4),

            realized_volatility=round(rv, 4),

            rolling_std=round(std, 4),

            volatility_regime=regime,

            expansion=expansion,

            compression=compression,

            volatility_score=score,

            explanation=explanation,

        )