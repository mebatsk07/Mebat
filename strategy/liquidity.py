from config import strategy


class LiquidityEngine:

    def score(self, ticker):

        quotes = ticker.get("quotes", {})

        bid = float(quotes.get("best_bid", 0))

        ask = float(quotes.get("best_ask", 0))

        volume = float(ticker.get("volume", 0))

        oi = float(ticker.get("oi", 0))

        bid_size = float(quotes.get("bid_size", 0))

        ask_size = float(quotes.get("ask_size", 0))

        # ---------------- Spread ----------------

        if ask == 0:

            spread = 100

        else:

            spread = ((ask - bid) / ask) * 100

        score = 100

        # Spread Penalty
        if spread > strategy.MAX_SPREAD_PERCENT:
            score -= 30

        # Volume Penalty
        if volume < strategy.MIN_VOLUME:
            score -= 25

        # OI Penalty
        if oi < strategy.MIN_OPEN_INTEREST:
            score -= 20

        # Bid Size Penalty
        if bid_size < strategy.MIN_BID_SIZE:
            score -= 15

        # Ask Size Penalty
        if ask_size < strategy.MIN_ASK_SIZE:
            score -= 10

        return {

            "score": max(score, 0),

            "spread": spread,

            "volume": volume,

            "oi": oi,

            "bid_size": bid_size,

            "ask_size": ask_size
        }