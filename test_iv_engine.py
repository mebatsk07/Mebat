from api.delta_client import DeltaClient
from strategy.iv_engine import IVEngine
from strategy.volatility import VolatilityEngine

client = DeltaClient()

response = client.get_tickers(
    contract_types=["call_options", "put_options"]
)

tickers = response["result"]

spot = None

for ticker in tickers:
    if ticker.get("underlying_asset_symbol") == "BTC":
        spot = float(ticker["spot_price"])
        break

# Replace this with your actual historical volatility
historical_volatility = 0.20

engine = IVEngine()

context = engine.analyze(
    tickers=tickers,
    spot=spot,
    historical_volatility=historical_volatility,
    days_to_expiry=1,
)

print("=" * 60)
print("IV ANALYSIS")
print("=" * 60)

print(f"ATM IV        : {context.atm_iv:.2%}")
print(f"Average IV    : {context.average_iv:.2%}")
print(f"Weighted IV   : {context.weighted_iv:.2%}")
print(f"IV/RV Ratio   : {context.iv_rv_ratio:.2f}")
print(f"Expected Move : ${context.expected_move:.2f}")
print(f"State         : {context.iv_state}")