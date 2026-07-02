from strategy.indicators import ema


class TrendEngine:

    def detect(self, df):

        df = df.copy()

        df["ema20"] = ema(df["close"], 20)

        df["ema50"] = ema(df["close"], 50)

        if df.iloc[-1]["ema20"] > df.iloc[-1]["ema50"]:
            return "UP"

        elif df.iloc[-1]["ema20"] < df.iloc[-1]["ema50"]:
            return "DOWN"

        return "SIDEWAYS"