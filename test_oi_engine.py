from api.delta_client import DeltaClient
from strategy.oi_engine import OIEngine

client = DeltaClient()

response = client.get_tickers(
    contract_types=["call_options", "put_options"]
)

tickers = response["result"]

# Find BTC spot from any ticker
spot = None

for ticker in tickers:
    if ticker.get("underlying_asset_symbol") == "BTC":
        spot = float(ticker["spot_price"])
        break

engine = OIEngine()

context = engine.analyze(
    tickers,
    spot,
)

print("\n========== OPTIONS SENTIMENT ==========")

print(f"Spot Price      : {spot:.2f}")
print(f"Put OI          : {context.total_put_oi:.2f}")
print(f"Call OI         : {context.total_call_oi:.2f}")

print(f"Put Volume      : {context.total_put_volume:.2f}")
print(f"Call Volume     : {context.total_call_volume:.2f}")

print(f"PCR OI          : {context.pcr_oi:.2f}")
print(f"PCR Volume      : {context.pcr_volume:.2f}")

print(f"ATM Put OI      : {context.atm_put_oi:.2f}")
print(f"ATM Call OI     : {context.atm_call_oi:.2f}")

print(f"ATM Put Volume  : {context.atm_put_volume:.2f}")
print(f"ATM Call Volume : {context.atm_call_volume:.2f}")

print(f"Bullish Score   : {context.bullish_score}")
print(f"Bearish Score   : {context.bearish_score}")

print(f"\nDirection        : {context.direction}")
print(f"Confidence       : {context.confidence:.1f}%")

print("\n========== MARKET STRUCTURE ==========")

print(f"Support Strike : {context.strongest_support}")
print(f"Resistance     : {context.strongest_resistance}")

print(f"Put Wall OI    : {context.put_wall:.2f}")
print(f"Call Wall OI   : {context.call_wall:.2f}")

print(f"\nBullish Score  : {context.bullish_score}")
print(f"Bearish Score  : {context.bearish_score}")

print(f"Confidence     : {context.confidence:.1f}%")

print(f"Direction      : {context.direction}")

print("\nReasons")

for reason in context.explanation:
    print("-", reason)