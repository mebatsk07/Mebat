import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import time

from engine.trading_engine import TradingEngine


class PaperTradingTest:

    def __init__(self):

        self.engine = TradingEngine()

        self.cycles = 3   # safe test limit

    def run(self):

        print("\n" + "=" * 60)
        print(" PAPER TRADING TEST MODE STARTED ")
        print("=" * 60)

        for i in range(self.cycles):

            print(f"\n--- CYCLE {i+1}/{self.cycles} ---\n")

            try:

                self.engine.run_cycle()

            except Exception as e:

                print("ERROR IN CYCLE:", e)

            time.sleep(2)  # short delay for testing

        print("\n" + "=" * 60)
        print(" TEST COMPLETED ")
        print("=" * 60)


# =====================================================
# RUN TEST
# =====================================================

if __name__ == "__main__":

    test = PaperTradingTest()

    test.run()