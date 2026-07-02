from sqlalchemy import select

from database.db import get_session
from database.models import BTCCandle


class Repository:

    def __init__(self):
        self.db = get_session()

    def candle_exists(self, symbol, timeframe, timestamp):

        stmt = select(BTCCandle).where(
            BTCCandle.symbol == symbol,
            BTCCandle.timeframe == timeframe,
            BTCCandle.timestamp == timestamp,
        )

        return self.db.execute(stmt).first() is not None

    def save_candles(self, candles):

        inserted = 0

        for candle in candles:

            if not self.candle_exists(
                candle.symbol,
                candle.timeframe,
                candle.timestamp,
            ):
                self.db.add(candle)
                inserted += 1

        self.db.commit()

        print(f"Inserted {inserted} new candles.")

    def save_option_snapshots(self, snapshots):

        self.db.add_all(snapshots)

        self.db.commit()

        print(f"Saved {len(snapshots)} option snapshots.")

    def close(self):
        self.db.close()