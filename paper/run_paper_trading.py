from engine.trading_engine import TradingEngine


def main():

    engine = TradingEngine()

    print("\n" + "=" * 60)
    print("STARTING PAPER TRADING SYSTEM")
    print("=" * 60)

    while True:

        try:

            engine.run_cycle()

        except Exception as e:

            print("\nSYSTEM ERROR:", e)

        # cycle delay (important)
        import time
        time.sleep(30)


if __name__ == "__main__":
    main()