from config import strategy

from api.delta_client import DeltaClient
from parsers.candidate_builder import build_candidate

from strategy.candidate_filter import CandidateFilter

from engine.candidate_scorer import CandidateScorer
from engine.candidate_ranker import CandidateRanker


class CandidateScanner:

    def __init__(self):

        self.client = DeltaClient()

        self.filter = CandidateFilter()

        self.scorer = CandidateScorer()

        self.ranker = CandidateRanker()

    # --------------------------------------------------
    # MAIN
    # --------------------------------------------------

    def scan(self, context):

        response = self.client.get_tickers(

            contract_types=[

                "call_options",

                "put_options",

            ]

        )

        tickers = response["result"]

        candidates = []

        rejected = []

        # -----------------------------------------
        # Strike Range
        # -----------------------------------------

        min_strike = context.spot * (

            1 - strategy.STRIKE_RANGE_PERCENT / 100

        )

        max_strike = context.spot * (

            1 + strategy.STRIKE_RANGE_PERCENT / 100

        )

        # -----------------------------------------
        # Scan Every Option
        # -----------------------------------------

        for ticker in tickers:

            try:

                candidate = build_candidate(ticker)

            except Exception:

                continue

            # -----------------------------------------
            # Strike Filter
            # -----------------------------------------

            if not (

                min_strike <= candidate.strike <= max_strike

            ):

                continue

            # -----------------------------------------
            # Candidate Filter
            # -----------------------------------------

            accepted, reason = self.filter.filter(

                candidate,

                context,

            )

            if not accepted:

                candidate.rejection_reason = reason

                rejected.append(candidate)

                continue

            # -----------------------------------------
            # Score Candidate
            # -----------------------------------------

            candidate = self.scorer.score(

                candidate,

                ticker,

                context,

            )

            candidates.append(candidate)

        # -----------------------------------------
        # Rank Candidates
        # -----------------------------------------

        candidates = self.ranker.rank(candidates)

        return candidates, rejected

    # --------------------------------------------------
    # Best Candidate
    # --------------------------------------------------

    def best_candidate(self, context):

        candidates, rejected = self.scan(context)

        if not candidates:

            return None

        return candidates[0]

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def statistics(

        self,

        accepted,

        rejected,

    ):

        return {

            "accepted": len(accepted),

            "rejected": len(rejected),

            "total": len(accepted) + len(rejected),

        }

    # --------------------------------------------------
    # Print Summary
    # --------------------------------------------------

    def print_summary(

        self,

        accepted,

        rejected,

    ):

        stats = self.statistics(

            accepted,

            rejected,

        )

        print()

        print("=" * 70)

        print("CANDIDATE SCANNER")

        print("=" * 70)

        print(f"Accepted : {stats['accepted']}")

        print(f"Rejected : {stats['rejected']}")

        print(f"Total    : {stats['total']}")

        if accepted:

            print()

            print("Top Candidates")

            print("-" * 70)

            for c in accepted[:10]:

                print(

                    f"{c.symbol:25}"

                    f" Score={c.final_score:6.2f}"

                    f" Premium={c.premium:8.2f}"

                    f" Delta={c.delta:7.4f}"

                )

        print("=" * 70)