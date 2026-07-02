from config import strategy


class PremiumRangeEngine:

    def get_range(self, regime: str):

        regime = regime.upper()

        # Sideways market
        if regime == "SIDEWAYS":
            return {
                "min": 12,
                "max": 20
            }

        # Strong downtrend
        elif regime == "STRONG_DOWNTREND":
            return {
                "min": 15,
                "max": 30
            }

        # Volatile range market
        elif regime == "VOLATILE_RANGE":
            return {
                "min": 20,
                "max": 35
            }

        # Panic selling
        elif regime == "PANIC_SELLING":
            return {
                "min": 25,
                "max": 40
            }

        # Strong uptrend
        elif regime == "STRONG_UPTREND":
            return {
                "min": 10,
                "max": 18
            }

        # Weak uptrend
        elif regime == "WEAK_UPTREND":
            return {
                "min": 10,
                "max": 20
            }

        # Default values
        return {
            "min": strategy.PREMIUM_MIN,
            "max": strategy.PREMIUM_MAX
        }