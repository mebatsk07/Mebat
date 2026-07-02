from database.data_loader import load_btc_dataframe
from strategy.reversal import ReversalEngine

df = load_btc_dataframe()

engine = ReversalEngine()

signal = engine.detect(df)

print("Reversal:", signal)