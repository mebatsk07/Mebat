from config import strategy
from .premium_range import PremiumRangeEngine


class CandidateFilter:

    def __init__(self):
        self.premium_engine = PremiumRangeEngine()

    def filter(self, candidate, regime):

        premium_range = self.premium_engine.get_range(regime)

        premium_min = premium_range["min"]
        premium_max = premium_range["max"]

        # Premium Filter
        if candidate.premium < premium_min:
            return False, (
                f"Premium {candidate.premium:.2f} "
                f"below {premium_min}"
            )

        if candidate.premium > premium_max:
            return False, (
                f"Premium {candidate.premium:.2f} "
                f"above {premium_max}"
            )

        # Delta Filter
        delta = abs(candidate.delta)

        if delta < strategy.DELTA_MIN:
            return False, "Delta too low"

        if delta > strategy.DELTA_MAX:
            return False, "Delta too high"

        return True, "Accepted"