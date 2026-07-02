from database.data_loader import load_btc_dataframe

from strategy.volatility import VolatilityEngine


df = load_btc_dataframe()

engine = VolatilityEngine()

result = engine.analyze(df)

print(result)