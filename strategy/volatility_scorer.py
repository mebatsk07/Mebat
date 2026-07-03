class VolatilityScorer:

    def score(self, candidate, context):

        ratio = context.iv_rv_ratio

        score = 100

        if ratio < 1.0:

            score = 30

        elif ratio < 1.2:

            score = 60

        elif ratio < 1.5:

            score = 80

        return {

            "iv_rv_ratio": ratio,

            "score": score

        }