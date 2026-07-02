from database.data_loader import load_btc_dataframe
from strategy.trend import TrendEngine

df = load_btc_dataframe()

engine = TrendEngine()

trend = engine.detect(df)

print("Current Trend:", trend)