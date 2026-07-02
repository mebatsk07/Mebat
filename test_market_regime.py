from database.data_loader import load_btc_dataframe

from strategy.market_regime import MarketRegime

df = load_btc_dataframe()

engine = MarketRegime()

print(engine.detect(df))