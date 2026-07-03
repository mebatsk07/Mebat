from strategy.premium_tracker import PremiumTracker


class PremiumScorer:

    def __init__(self):

        self.tracker = PremiumTracker()

    def score(self, ticker, regime):

        self.tracker.update(ticker)

        symbol = ticker["symbol"]

        data = self.tracker.get(symbol)

        premium = data["current"]

        expansion = self.tracker.expansion(symbol)

        score = 100

        if regime == "STRONG_TREND":

            if premium < 15:
                score = 20
            elif premium < 30:
                score = 60

        elif regime == "SIDEWAYS":

            if premium < 10:
                score = 40

        elif regime == "VOLATILE_RANGE":

            if premium < 25:
                score = 30

        return {

            "premium": premium,

            "expansion": expansion,

            "score": score

        }