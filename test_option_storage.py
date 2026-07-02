from collectors.option_market_collector import OptionMarketCollector
from parsers.option_parser import parse_option_snapshot
from database.repository import Repository

collector = OptionMarketCollector()

tickers = collector.snapshot()

snapshots = [
    parse_option_snapshot(ticker)
    for ticker in tickers
]

repo = Repository()

repo.save_option_snapshots(snapshots)

repo.close()

print(f"Saved {len(snapshots)} option snapshots.")