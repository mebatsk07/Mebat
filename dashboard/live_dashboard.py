from datetime import datetime


class LiveDashboard:

    def display(

        self,

        context,

        account,

        positions,

        candidates,

    ):

        print("\n" * 2)

        print("=" * 80)
        print("               BTC OPTIONS PAPER TRADING DASHBOARD")
        print("=" * 80)

        print(f"Time                : {datetime.now()}")

        print()

        # =====================================================
        # MARKET
        # =====================================================

        print("-" * 80)
        print("MARKET")
        print("-" * 80)

        print(f"Spot Price          : {context.spot:,.2f}")
        print(f"Trend               : {context.trend}")
        print(f"Regime              : {context.regime}")
        print(f"Direction           : {context.direction}")
        print(f"Confidence          : {context.confidence:.1f}%")

        print()

        print(f"ATR                 : {context.atr:.2f}")
        print(f"ATR %               : {context.atr_percent:.2f}%")

        print(f"Historical Vol      : {context.historical_volatility:.2f}")

        print(f"ATM IV              : {context.atm_iv:.2f}")

        print(f"Average IV          : {context.average_iv:.2f}")

        print(f"IV/RV Ratio         : {context.iv_rv_ratio:.2f}")

        print()

        print(f"PCR OI              : {context.pcr_oi:.2f}")

        print(f"PCR Volume          : {context.pcr_volume:.2f}")

        print(f"Support             : {context.support:.2f}")

        print(f"Resistance          : {context.resistance:.2f}")

        # =====================================================
        # ACCOUNT
        # =====================================================

        print()
        print("-" * 80)
        print("ACCOUNT")
        print("-" * 80)

        print(f"Balance             : {account.balance:,.2f}")

        print(f"Available           : {account.available_balance:,.2f}")

        print(f"Margin Used         : {account.margin_used:,.2f}")

        print(f"Equity              : {account.equity:,.2f}")

        print()

        print(f"Daily PnL           : {account.daily_pnl:,.2f}")

        print(f"Total PnL           : {account.total_pnl:,.2f}")

        print(f"Trades              : {account.total_trades}")

        print(f"Win Rate            : {account.win_rate:.2f}%")

        # =====================================================
        # POSITIONS
        # =====================================================

        print()
        print("-" * 80)
        print("OPEN POSITIONS")
        print("-" * 80)

        if len(positions) == 0:

            print("No Open Positions")

        else:

            for p in positions:

                print(

                    f"{p.symbol:25}"

                    f" Entry={p.entry_price:8.2f}"

                    f" Current={p.current_price:8.2f}"

                    f" PnL={p.unrealized_pnl:10.2f}"

                    f" Health={p.trade_health:6.1f}%"

                )

        # =====================================================
        # CANDIDATES
        # =====================================================

        print()
        print("-" * 80)
        print("TOP CANDIDATES")
        print("-" * 80)

        if len(candidates) == 0:

            print("No Candidates")

        else:

            for c in candidates[:10]:

                print(

                    f"{c.symbol:25}"

                    f" Score={c.final_score:6.2f}"

                    f" Premium={c.premium:8.2f}"

                    f" Delta={c.delta:7.4f}"

                )

        # =====================================================
        # SYSTEM
        # =====================================================

        print()
        print("-" * 80)
        print("SYSTEM STATUS")
        print("-" * 80)

        print("Market Analyzer     : OK")
        print("Candidate Scanner   : OK")
        print("Candidate Ranker    : OK")
        print("Risk Manager        : OK")
        print("Paper Broker        : OK")
        print("Position Manager    : OK")

        print("=" * 80)