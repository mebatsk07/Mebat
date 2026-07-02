from collectors.btc_collector import BTCCollector
from parsers.candle_parser import parse_candles
from database.repository import Repository

collector = BTCCollector()

response = collector.latest_day()

candles = parse_candles(response["result"])

repo = Repository()

repo.save_candles(candles)

repo.close()

print(f"Saved {len(candles)} candles into SQLite.")