import sys
import os

# FORCE project root into path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tests.test_paper_trading import PaperTradingTest


if __name__ == "__main__":

    test = PaperTradingTest()

    test.run()