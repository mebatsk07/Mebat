class ThetaEngine:

    def score(self, ticker):

        theta = abs(
            float(
                ticker.get("greeks", {})
                .get("theta", 0)
            )
        )

        if theta >= 25:
            return 100

        elif theta >= 15:
            return 80

        elif theta >= 10:
            return 60

        elif theta >= 5:
            return 40

        return 20