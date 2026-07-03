from config import strategy

from api.delta_client import DeltaClient
from parsers.candidate_builder import build_candidate
from strategy.candidate_filter import CandidateFilter

class CandidateRanker:

    def __init__(self):

        # ---------------------------------------------
        # Weightage of each scoring engine
        # Total = 100
        # ---------------------------------------------
        self.weights = {

            "delta": 20,

            "premium": 20,

            "theta": 15,

            "liquidity": 15,

            "trend": 10,

            "volatility": 10,

            "risk": 10,

        }

    # --------------------------------------------------
    # Rank Candidates
    # --------------------------------------------------

    def rank(self, candidates):

        for candidate in candidates:

            candidate.final_score = self.calculate(candidate)

        candidates.sort(

            key=lambda c: c.final_score,

            reverse=True,

        )

        return candidates

    # --------------------------------------------------
    # Calculate Final Score
    # --------------------------------------------------

    def calculate(self, candidate):

        weighted_total = (

            candidate.delta_score * self.weights["delta"]

            + candidate.premium_score * self.weights["premium"]

            + candidate.theta_score * self.weights["theta"]

            + candidate.liquidity_score * self.weights["liquidity"]

            + candidate.trend_score * self.weights["trend"]

            + candidate.volatility_score * self.weights["volatility"]

            + candidate.risk_score * self.weights["risk"]

        )

        # Each score is between 0-100
        # Total weight = 100
        final_score = weighted_total / 100

        return round(final_score, 2)

    # --------------------------------------------------
    # Best Candidate
    # --------------------------------------------------

    def best(self, candidates):

        if not candidates:

            return None

        return max(

            candidates,

            key=lambda c: c.final_score,

        )

    # --------------------------------------------------
    # Top N Candidates
    # --------------------------------------------------

    def top(self, candidates, n=5):

        ranked = self.rank(candidates)

        return ranked[:n]

    # --------------------------------------------------
    # Print Rankings
    # --------------------------------------------------

    def print_rankings(self, candidates, limit=10):

        print()

        print("=" * 70)
        print("CANDIDATE RANKINGS")
        print("=" * 70)

        ranked = self.rank(candidates)

        for i, candidate in enumerate(ranked[:limit], start=1):

            print(
                f"{i:2}. "
                f"{candidate.symbol:25}"
                f" Score={candidate.final_score:6.2f}"
                f" Premium={candidate.premium:8.2f}"
                f" Delta={candidate.delta:7.4f}"
            )

        print("=" * 70)