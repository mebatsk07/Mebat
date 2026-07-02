from strategy.indicators import ema


class ReversalEngine:

    def detect(self, df):

        df = df.copy()

        df["ema20"] = ema(df["close"], 20)
        df["ema50"] = ema(df["close"], 50)

        previous = df.iloc[-2]
        current = df.iloc[-1]

        # Bullish crossover
        if (
            previous["ema20"] < previous["ema50"]
            and current["ema20"] > current["ema50"]
            and current["close"] > current["ema20"]
        ):
            return "BULLISH"

        # Bearish crossover
        if (
            previous["ema20"] > previous["ema50"]
            and current["ema20"] < current["ema50"]
            and current["close"] < current["ema20"]
        ):
            return "BEARISH"

        return "NONE"