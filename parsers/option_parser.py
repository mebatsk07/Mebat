from datetime import datetime, timezone

for ticker in tickers:
    if "volume" not in ticker:
        print("Missing volume:", ticker["symbol"])

from database.models import OptionSnapshot


def parse_option_snapshot(ticker):

    quotes = ticker["quotes"]
    greeks = ticker["greeks"]

    return OptionSnapshot(
        timestamp=datetime.fromtimestamp(
            ticker["timestamp"] / 1_000_000,
            tz=timezone.utc,
        ),

        product_id=ticker["product_id"],

        symbol=ticker["symbol"],
        
        quotes = ticker.get("quotes", {}),

        greeks = ticker.get("greeks", {}),

        contract_type=ticker["contract_type"],

        strike=float(ticker["strike_price"]),

        spot_price=float(ticker["spot_price"]),

        bid=float(quotes.get("best_bid", 0.0)),
        
        ask=float(quotes.get("best_ask", 0.0)),

        mark_price=float(ticker.get("mark_price", 0.0)),

        mark_iv=float(quotes.get("mark_iv", 0.0)),

        delta=float(greeks.get("delta", 0.0)),
        
        gamma=float(greeks.get("gamma", 0.0)),
        
        theta=float(greeks.get("theta", 0.0)),
        
        vega=float(greeks.get("vega", 0.0)),

        volume=float(ticker.get("volume", 0.0)),

        open_interest=float(ticker.get("oi", 0.0)),
    )