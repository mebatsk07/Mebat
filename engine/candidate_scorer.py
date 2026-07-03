from dataclasses import dataclass

from strategy.indicators import clamp


# =====================================================
# SCORED CANDIDATE
# =====================================================

@dataclass
class ScoredCandidate:

    symbol: str

    strike: float

    premium: float

    delta: float

    iv: float

    volume: float

    oi: float

    liquidity_score: float

    theta_score: float

    delta_score: float

    iv_score: float

    final_score: float


# =====================================================
# CANDIDATE SCORER
# =====================================================

class CandidateScorer:

    def __init__(self):

        pass

    # -------------------------------------------------
    # DELTA SCORE
    # -------------------------------------------------

    def _score_delta(self, delta):

        d = abs(delta)

        target = 0.30

        distance = abs(d - target)

        score = 100 - (distance * 250)

        return clamp(score)

    # -------------------------------------------------
    # IV SCORE
    # -------------------------------------------------

    def _score_iv(self, iv):

        if iv >= 0.8:
            return 100

        if iv >= 0.6:
            return 80

        if iv >= 0.4:
            return 60

        if iv >= 0.2:
            return 40

        return 20

    # -------------------------------------------------
    # LIQUIDITY SCORE
    # -------------------------------------------------

    def _score_liquidity(self, volume, oi):

        score = 100

        if volume < 10:
            score -= 30

        if oi < 50:
            score -= 25

        if oi < 20:
            score -= 20

        return clamp(score)

    # -------------------------------------------------
    # THETA SCORE (SELLING EDGE)
    # -------------------------------------------------

    def _score_theta(self, theta):

        theta = abs(theta)

        if theta >= 25:
            return 100

        if theta >= 15:
            return 80

        if theta >= 10:
            return 60

        if theta >= 5:
            return 40

        return 20

    # -------------------------------------------------
    # FINAL SCORING
    # -------------------------------------------------

    def score(self, candidate):

        delta_score = self._score_delta(candidate.delta)

        iv_score = self._score_iv(candidate.iv)

        liquidity_score = self._score_liquidity(
            candidate.volume,
            candidate.oi,
        )

        theta_score = self._score_theta(candidate.delta * 10)

        final_score = (

            delta_score * 0.30 +

            iv_score * 0.25 +

            liquidity_score * 0.25 +

            theta_score * 0.20

        )

        return ScoredCandidate(

            symbol=candidate.symbol,

            strike=candidate.strike,

            premium=candidate.premium,

            delta=candidate.delta,

            iv=candidate.iv,

            volume=candidate.volume,

            oi=candidate.oi,

            liquidity_score=liquidity_score,

            theta_score=theta_score,

            delta_score=delta_score,

            iv_score=iv_score,

            final_score=round(final_score, 2),

        )