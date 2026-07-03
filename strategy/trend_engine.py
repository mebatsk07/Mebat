from dataclasses import dataclass

from strategy.indicators import (
    ema,
    slope,
    ema_distance,
    higher_high,
    higher_low,
    lower_high,
    lower_low,
)


# =====================================================
# TREND CONTEXT
# =====================================================

@dataclass
class TrendContext:

    trend: str

    strength: float

    ema20: float

    ema50: float

    ema200: float

    price: float

    ema20_slope: float

    ema50_slope: float

    distance_from_ema20: float

    distance_from_ema50: float

    higher_high: bool

    higher_low: bool

    lower_high: bool

    lower_low: bool

    explanation: list[str]


# =====================================================
# TREND ENGINE
# =====================================================

class TrendEngine:

    def analyze(self, df):

        df = df.copy()

        # -----------------------------
        # Calculate EMAs
        # -----------------------------

        df["ema20"] = ema(df["close"], 20)

        df["ema50"] = ema(df["close"], 50)

        df["ema200"] = ema(df["close"], 200)

        latest = df.iloc[-1]

        price = float(latest["close"])

        ema20 = float(latest["ema20"])

        ema50 = float(latest["ema50"])

        ema200 = float(latest["ema200"])

        # -----------------------------
        # EMA Slopes
        # -----------------------------

        ema20_slope = float(
            slope(df["ema20"], 5).iloc[-1]
        )

        ema50_slope = float(
            slope(df["ema50"], 5).iloc[-1]
        )

        # -----------------------------
        # Distance from EMA
        # -----------------------------

        distance20 = float(
            ema_distance(price, ema20)
        )

        distance50 = float(
            ema_distance(price, ema50)
        )

        # -----------------------------
        # Market Structure
        # -----------------------------

        hh = higher_high(df)

        hl = higher_low(df)

        lh = lower_high(df)

        ll = lower_low(df)

        # -----------------------------
        # Trend Score
        # -----------------------------

        bullish = 0

        bearish = 0

        explanation = []

        # EMA Alignment

        if ema20 > ema50 > ema200:

            bullish += 35

            explanation.append(
                "EMA alignment bullish"
            )

        elif ema20 < ema50 < ema200:

            bearish += 35

            explanation.append(
                "EMA alignment bearish"
            )

        # Price Position

        if price > ema20:

            bullish += 15

        else:

            bearish += 15

        if price > ema50:

            bullish += 10

        else:

            bearish += 10

        # EMA Slopes

        if ema20_slope > 0:

            bullish += 15

        else:

            bearish += 15

        if ema50_slope > 0:

            bullish += 10

        else:

            bearish += 10

        # Market Structure

        if hh:

            bullish += 8

            explanation.append(
                "Higher High"
            )

        if hl:

            bullish += 7

            explanation.append(
                "Higher Low"
            )

        if lh:

            bearish += 8

            explanation.append(
                "Lower High"
            )

        if ll:

            bearish += 7

            explanation.append(
                "Lower Low"
            )

        # -----------------------------
        # Final Trend
        # -----------------------------

        trend = "SIDEWAYS"

        strength = 50

        if bullish > bearish:

            trend = "UP"

            strength = bullish

        elif bearish > bullish:

            trend = "DOWN"

            strength = bearish

        strength = round(

            min(strength, 100),

            2,

        )

        # -----------------------------
        # Return Context
        # -----------------------------

        return TrendContext(

            trend=trend,

            strength=strength,

            ema20=ema20,

            ema50=ema50,

            ema200=ema200,

            price=price,

            ema20_slope=ema20_slope,

            ema50_slope=ema50_slope,

            distance_from_ema20=distance20,

            distance_from_ema50=distance50,

            higher_high=hh,

            higher_low=hl,

            lower_high=lh,

            lower_low=ll,

            explanation=explanation,

        )