from collectors.option_market_collector import OptionMarketCollector

collector = OptionMarketCollector()

tickers = collector.snapshot()

print(f"Received {len(tickers)} live tickers")

print()

print(tickers[0])