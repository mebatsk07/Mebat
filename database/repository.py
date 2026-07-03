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

    def save_market_snapshot(self, snapshot):

        self.db.add(snapshot)

        self.db.commit()

        print("Saved market snapshot.")

    def save_paper_trade(self, trade):

        self.db.add(trade)

        self.db.commit()    
    def update_paper_trade(self, trade):

         self.db.commit()    

    def close(self):
        self.db.close()

    def get_open_trade(self, symbol):

        stmt = select(PaperTrade).where(

            PaperTrade.symbol == symbol,

            PaperTrade.exit_time == None

        )

        result = self.db.execute(stmt)

        return result.scalar_one_or_none()    
    
    def save_decision(self, decision):

        self.db.add(decision)

        self.db.commit()

    def daily_statistics(self):

        total = self.db.query(PaperTrade).count()

        closed = self.db.query(PaperTrade).filter(
        PaperTrade.exit_time != None
        ).all()

        wins = len([t for t in closed if t.pnl > 0])

        losses = len([t for t in closed if t.pnl <= 0])

        pnl = sum(t.pnl for t in closed)

        return {

        "total": total,

        "wins": wins,

        "losses": losses,

        "net_pnl": pnl,

    }    