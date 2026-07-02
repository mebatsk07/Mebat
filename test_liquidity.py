from api.delta_client import DeltaClient
from strategy.liquidity import LiquidityEngine

client = DeltaClient()

engine = LiquidityEngine()

tickers = client.get_tickers(
    ["call_options", "put_options"]
)["result"]

result = engine.score(tickers[0])

print(result)