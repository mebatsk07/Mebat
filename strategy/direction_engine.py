from dataclasses import dataclass

from models.market_context import MarketContext


@dataclass
class DirectionDecision:

    direction: str

    confidence: float

    trade_allowed: bool

    score: float

    reasons: list


class DirectionEngine:

    def analyze(self, context: MarketContext):

        bullish = 0
        bearish = 0

        reasons = []

        # ------------------------
        # Trend
        # ------------------------

        if context.trend == "UP":
            bullish += 30
            reasons.append("Trend Up")

        elif context.trend == "DOWN":
            bearish += 30
            reasons.append("Trend Down")

        # ------------------------
        # Market Regime
        # ------------------------

        if context.regime == "SIDEWAYS":
            bullish += 5
            bearish += 5
            reasons.append("Sideways Market")

        elif context.regime == "STRONG_UPTREND":
            bullish += 15

        elif context.regime == "STRONG_DOWNTREND":
            bearish += 15

        elif context.regime == "VOLATILE_RANGE":
            bullish += 3
            bearish += 3
            reasons.append("High Volatility")

        # ------------------------
        # IV
        # ------------------------

        if context.iv_rv_ratio >= 1.5:
            bullish += 10
            bearish += 10
            reasons.append("Premium Rich")

        elif context.iv_rv_ratio < 1.0:
            reasons.append("IV Cheap")

        # ------------------------
        # OI
        # ------------------------

        bullish += context.bullish_score * 0.30
        bearish += context.bearish_score * 0.30

        # ------------------------
        # Volatility
        # ------------------------

        if context.atr_percent < 0.40:
            bullish += 10
            bearish += 10
            reasons.append("Low ATR")

        elif context.atr_percent > 1.20:
            bullish -= 5
            bearish -= 5
            reasons.append("ATR High")

        # ------------------------
        # Decision
        # ------------------------

        score = max(bullish, bearish)

        total = bullish + bearish

        confidence = 0

        if total > 0:
            confidence = round(score / total * 100, 1)

        direction = "NEUTRAL"

        if bearish > bullish:

            if confidence > 75:
                direction = "STRONG_BEARISH"

            else:
                direction = "BEARISH"

        elif bullish > bearish:

            if confidence > 75:
                direction = "STRONG_BULLISH"

            else:
                direction = "BULLISH"

        trade_allowed = (
            confidence >= 65
            and context.iv_rv_ratio >= 1.3
        )

        return DirectionDecision(

            direction=direction,

            confidence=confidence,

            trade_allowed=trade_allowed,

            score=score,

            reasons=reasons,
        )