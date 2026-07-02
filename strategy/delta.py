from config import strategy


class DeltaEngine:

    def score(self, ticker):

        delta = abs(
            float(
                ticker.get("greeks", {})
                .get("delta", 0)
            )
        )

        target = (
            strategy.DELTA_MIN +
            strategy.DELTA_MAX
        ) / 2

        distance = abs(delta - target)

        score = max(
            0,
            100 - distance * 3000
        )

        return {

            "delta": delta,

            "score": round(score, 2)
        }