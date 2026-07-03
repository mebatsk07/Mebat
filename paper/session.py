from datetime import datetime
from config import strategy
import time

from engine.trading_engine import TradingEngine
from paper.account import PaperAccount
from paper.broker import PaperBroker


class PaperTradingSession:

    def __init__(self):

        self.account = PaperAccount()

        self.broker = PaperBroker()

        self.engine = TradingEngine()

        self.context = None

        self.dashboard = Dashboard()

        self.journal = PaperJournal()

        self.monitor = PositionMonitor(
            self.account,
            self.broker,
            self.journal,
        )

    def start(self):

        print("=" * 60)
        print("BTC OPTIONS PAPER TRADING SESSION")
        print("=" * 60)

        while True:

            now = datetime.now()

            print(f"\n{now}")

            try:

                self.run_cycle()

            except Exception as e:

                print("Session Error:", e)

            time.sleep(strategy.MONITOR_INTERVAL_SECONDS)

    def run_cycle(self):

       # 1
        self.update_market()

    # 2
        self.monitor_positions()

    # 3
        self.find_trade()

    # 4
        self.update_dashboard()

    # 5
        self.save_cycle()

        pass
    def update_market(self):

        self.context = self.engine.build_market_context()

    def monitor_positions(self):

        self.monitor.update(self.context)
    def find_trade(self):

        if not self.context.trade_allowed:
            return

        candidate = self.engine.find_best_candidate(self.context)

        if candidate is None:
            return

        self.broker.open_position(candidate)    

    def update_dashboard(self):

         self.dashboard.render(
            account=self.account,
            context=self.context,
            broker=self.broker,
         )    
    def save_cycle(self):

        self.journal.save_engine_cycle(
            self.context,
            self.account,
    )     