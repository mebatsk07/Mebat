from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Dict, Any

from paper.paper_position import PaperPosition


# =====================================================
# TRADE RECORD
# =====================================================

@dataclass
class TradeRecord:

    symbol: str

    side: str

    entry_price: float

    exit_price: float

    quantity: int

    pnl: float

    entry_time: str

    exit_time: str

    exit_reason: str

    trade_health: float

    strike: float


# =====================================================
# TRADING JOURNAL
# =====================================================

class TradingJournal:

    def __init__(self):

        self.trades: List[TradeRecord] = []

    # -------------------------------------------------
    # RECORD TRADE
    # -------------------------------------------------

    def record(self, position: PaperPosition):

        if position.status != "CLOSED":

            return

        record = TradeRecord(

            symbol=position.symbol,

            side=position.side,

            entry_price=position.entry_price,

            exit_price=position.exit_price,

            quantity=position.quantity,

            pnl=position.unrealized_pnl,

            entry_time=str(position.entry_time),

            exit_time=str(position.exit_time),

            exit_reason=position.exit_reason,

            trade_health=position.trade_health,

            strike=position.strike,

        )

        self.trades.append(record)

    # -------------------------------------------------
    # GET PERFORMANCE SUMMARY
    # -------------------------------------------------

    def summary(self) -> Dict[str, Any]:

        if not self.trades:

            return {

                "total_trades": 0,

                "win_rate": 0,

                "total_pnl": 0,

            }

        wins = 0

        total_pnl = 0

        for t in self.trades:

            total_pnl += t.pnl

            if t.pnl > 0:

                wins += 1

        win_rate = wins / len(self.trades) * 100

        return {

            "total_trades": len(self.trades),

            "win_rate": round(win_rate, 2),

            "total_pnl": round(total_pnl, 2),

        }

    # -------------------------------------------------
    # EXPORT ALL TRADES
    # -------------------------------------------------

    def export(self) -> List[Dict]:

        return [

            asdict(t)

            for t in self.trades

        ]

    # -------------------------------------------------
    # PRINT REPORT
    # -------------------------------------------------

    def print_report(self):

        s = self.summary()

        print()

        print("=" * 60)

        print("TRADING JOURNAL REPORT")

        print("=" * 60)

        print(f"Total Trades : {s['total_trades']}")

        print(f"Win Rate     : {s['win_rate']} %")

        print(f"Total PnL    : {s['total_pnl']}")

        print("=" * 60)