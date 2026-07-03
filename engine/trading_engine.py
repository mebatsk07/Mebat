from analysis.market_analyzer import MarketAnalyzer
from dashboard.live_dashboard import LiveDashboard

from engine.candidate_scanner import CandidateScanner
from engine.risk_manager import RiskManager

from paper.broker import PaperBroker
from paper.position_manager import PositionManager


class TradingEngine:

    def __init__(self):

        self.market_analyzer = MarketAnalyzer()

        self.scanner = CandidateScanner()

        self.risk = RiskManager()

        self.position_manager = PositionManager()

        self.broker = PaperBroker(
            self.position_manager
        )

        self.dashboard = LiveDashboard()

        self.context = None

    # --------------------------------------------------
    # Build Market Context
    # --------------------------------------------------

    def build_market_context(self):

        self.context = self.market_analyzer.analyze()

        return self.context

    # --------------------------------------------------
    # Scan Market
    # --------------------------------------------------

    def scan_market(self):

        if self.context is None:

            self.build_market_context()

        candidates, rejected = self.scanner.scan(
            self.context
        )

        return candidates, rejected

    # --------------------------------------------------
    # Best Trade
    # --------------------------------------------------

    def find_best_trade(self, candidates):

        if not candidates:

            print()
            print("No valid trade found.")

            return None

        best = candidates[0]

        print()
        print("=" * 70)
        print("BEST TRADE")
        print("=" * 70)

        print(f"Symbol      : {best.symbol}")
        print(f"Strike      : {best.strike}")
        print(f"Premium     : {best.premium:.2f}")
        print(f"Delta       : {best.delta:.4f}")
        print(f"Final Score : {best.final_score:.2f}")

        print("=" * 70)

        return best

    # --------------------------------------------------
    # Execute Trade
    # --------------------------------------------------

    def execute_trade(self, candidates):

        best = self.find_best_trade(candidates)

        if best is None:

            return None

        allowed, reason = self.risk.validate(

            best,

            self.context,

            self.broker.account,

            self.position_manager,

        )

        if not allowed:

            print()
            print("=" * 70)
            print("TRADE REJECTED")
            print("=" * 70)
            print(reason)
            print("=" * 70)

            return None

        position = self.broker.sell_option(

            best,

            self.context,

        )

        return position

    # --------------------------------------------------
    # Update Positions
    # --------------------------------------------------

    def update_positions(self):

        if self.context is None:

            return

        self.position_manager.update(

            self.context

        )

    # --------------------------------------------------
    # Run Trading Cycle
    # --------------------------------------------------

    def run_cycle(self):

        print()
        print("=" * 70)
        print("STARTING NEW TRADING CYCLE")
        print("=" * 70)

        # 1. Build market context
        self.build_market_context()

        # 2. Scan market ONCE
        candidates, rejected = self.scan_market()

        # 3. Execute best trade
        self.execute_trade(candidates)

        # 4. Update existing positions
        self.update_positions()

        # 5. Display dashboard
        self.dashboard.display(

            self.context,

            self.broker.account,

            self.position_manager.get_open_positions(),

            candidates,

        )

        print()
        print("=" * 70)
        print("TRADING CYCLE COMPLETE")
        print("=" * 70)