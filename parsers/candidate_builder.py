from models.option_candidate import OptionCandidate


def build_candidate(ticker):

    quotes = ticker.get("quotes", {})

    greeks = ticker.get("greeks", {})

    return OptionCandidate(

        symbol=ticker["symbol"],

        product_id=ticker["product_id"],

        option_type=ticker["contract_type"],

        strike=float(ticker["strike_price"]),

        expiry=ticker.get("settlement_time", ""),

        premium=float(ticker.get("mark_price", 0)),

        bid=float(quotes.get("best_bid", 0)),

        ask=float(quotes.get("best_ask", 0)),

        spot=float(ticker.get("spot_price", 0)),

        delta=float(greeks.get("delta", 0)),

        gamma=float(greeks.get("gamma", 0)),

        theta=float(greeks.get("theta", 0)),

        vega=float(greeks.get("vega", 0)),

        iv=float(quotes.get("mark_iv", 0)),

        volume=float(ticker.get("volume", 0)),

        open_interest=float(ticker.get("oi", 0)),
    )