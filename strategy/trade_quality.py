from dataclasses import dataclass

from models.market_context import MarketContext
from models.option_candidate import OptionCandidate


@dataclass
class TradeQuality:

    score: float

    recommendation: str

    reasons: list

    trade_allowed: bool


class TradeQualityEngine:

    def evaluate(
        self,
        context: MarketContext,
        candidate: OptionCandidate,
    ):

        score = 0

        reasons = []

        # -------------------------
        # Premium
        # -------------------------

        if 15 <= candidate.premium <= 30:
            score += 20
            reasons.append("Premium Ideal")

        elif 12 <= candidate.premium <= 35:
            score += 15

        # -------------------------
        # Delta
        # -------------------------

        delta = abs(candidate.delta)

        if 0.02 <= delta <= 0.05:
            score += 15
            reasons.append("Delta Ideal")

        elif delta <= 0.08:
            score += 10

        # -------------------------
        # Theta
        # -------------------------

        if abs(candidate.theta) >= 120:
            score += 15
            reasons.append("Strong Theta")

        # -------------------------
        # Liquidity
        # -------------------------

        spread = candidate.ask - candidate.bid

        if spread <= candidate.premium * 0.08:
            score += 10
            reasons.append("Tight Spread")

        # -------------------------
        # IV
        # -------------------------

        if context.iv_rv_ratio >= 1.5:
            score += 15
            reasons.append("IV Elevated")

        # -------------------------
        # Trend
        # -------------------------

        if context.direction.startswith("BEAR"):
            if candidate.option_type == "call_options":
                score += 10
                reasons.append("Call Sell")

        if context.direction.startswith("BULL"):
            if candidate.option_type == "put_options":
                score += 10
                reasons.append("Put Sell")

        # -------------------------
        # Time Filter
        # -------------------------

        if context.trade_allowed:
            score += 10

        recommendation = "REJECT"

        if score >= 90:
            recommendation = "A+"

        elif score >= 80:
            recommendation = "A"

        elif score >= 70:
            recommendation = "B"

        elif score >= 60:
            recommendation = "WATCH"

        trade_allowed = score >= 70

        return TradeQuality(
            score=score,
            recommendation=recommendation,
            reasons=reasons,
            trade_allowed=trade_allowed,
        )