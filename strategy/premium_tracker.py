from collections import defaultdict
from datetime import datetime


class PremiumTracker:

    def __init__(self):

        self.history = defaultdict(dict)

    def update(self, ticker):

        symbol = ticker["symbol"]

        premium = float(ticker.get("mark_price", 0))

        bid = float(
            ticker.get("quotes", {}).get("best_bid", 0)
        )

        ask = float(
            ticker.get("quotes", {}).get("best_ask", 0)
        )

        volume = float(ticker.get("volume", 0))

        oi = float(ticker.get("oi", 0))

        iv = float(
            ticker.get("quotes", {}).get("mark_iv", 0)
        )

        delta = float(
            ticker.get("greeks", {}).get("delta", 0)
        )

        theta = float(
            ticker.get("greeks", {}).get("theta", 0)
        )

        now = datetime.utcnow()

        if symbol not in self.history:

            self.history[symbol] = {

                "lowest": premium,
                "highest": premium,
                "current": premium,

                "lowest_time": now,
                "highest_time": now,

                "volume": volume,
                "oi": oi,

                "iv": iv,

                "delta": delta,

                "theta": theta,

                "bid": bid,

                "ask": ask,

                "updates": 1,
            }

            return

        r = self.history[symbol]

        r["updates"] += 1

        r["current"] = premium

        r["volume"] = volume

        r["oi"] = oi

        r["iv"] = iv

        r["delta"] = delta

        r["theta"] = theta

        r["bid"] = bid

        r["ask"] = ask

        if premium < r["lowest"]:

            r["lowest"] = premium

            r["lowest_time"] = now

        if premium > r["highest"]:

            r["highest"] = premium

            r["highest_time"] = now

    def expansion(self, symbol):

        r = self.history[symbol]

        if r["lowest"] == 0:

            return 0

        return r["current"] / r["lowest"]

    def spread_percent(self, symbol):

        r = self.history[symbol]

        if r["ask"] == 0:

            return 100

        return (r["ask"] - r["bid"]) / r["ask"] * 100

    def get(self, symbol):

        return self.history.get(symbol)