class ThetaEngine:

    def score(self, ticker):

        theta = abs(
            float(
                ticker.get("greeks", {})
                .get("theta", 0)
            )
        )

        if theta >= 25:
            score = 100

        elif theta >= 15:
            score = 80

        elif theta >= 10:
            score = 60

        elif theta >= 5:
            score = 40

        else:
            score = 20

        return {

            "theta": theta,

            "score": score

        }