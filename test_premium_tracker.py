from api.delta_client import DeltaClient
from strategy.premium_tracker import PremiumTracker

client = DeltaClient()
tracker = PremiumTracker()

tickers = client.get_tickers(
    ["call_options", "put_options"]
)["result"]

for ticker in tickers:
    tracker.update(ticker)

sample = tickers[0]["symbol"]

print(tracker.get(sample))

print(
    "Expansion:",
    tracker.expansion(sample)
)

print(
    "Spread:",
    tracker.spread_percent(sample)
)