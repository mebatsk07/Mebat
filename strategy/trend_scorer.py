class TrendScorer:

    def score(self, candidate, context):

        score = 50

        if context.direction == "BULLISH":

            if candidate.option_type == "put_options":
                score = 100
            else:
                score = 30

        elif context.direction == "BEARISH":

            if candidate.option_type == "call_options":
                score = 100
            else:
                score = 30

        return {

            "trend": context.direction,

            "score": score

        }