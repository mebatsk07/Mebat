from datetime import datetime


# =====================================================
# LIVE DASHBOARD
# =====================================================

class LiveDashboard:

    def __init__(self):

        pass

    # -------------------------------------------------
    # MAIN DISPLAY
    # -------------------------------------------------

    def display(
        self,
        context,
        account,
        positions,
        candidates,
    ):

        print("\n" * 2)

        print("=" * 80)

        print(" LIVE TRADING DASHBOARD ")

        print("=" * 80)

        self._print_time()

        self._print_market(context)

        self._print_account(account)

        self._print_positions(positions)

        self._print_candidates(candidates)

        print("=" * 80)

    # -------------------------------------------------
    # TIME
    # -------------------------------------------------

    def _print_time(self):

        now = datetime.utcnow()

        print(f"\n🕒 Time (UTC): {now}")

    # -------------------------------------------------
    # MARKET SNAPSHOT
    # -------------------------------------------------

    def _print_market(self, context):

        print("\n📊 MARKET SNAPSHOT")

        print("-" * 40)

        print(f"Spot        : {context.spot}")

        print(f"Trend       : {context.trend}")

        print(f"ATR %       : {context.atr_percent:.2f}")

        print(f"IV State    : {context.iv_state}")

        print(f"PCR OI      : {context.pcr_oi:.2f}")

        print(f"Direction   : {context.direction}")

        print(f"Confidence  : {context.confidence:.2f}")

        print(f"Trade Allowed: {context.trade_allowed}")

        if context.reasons:

            print("\n⚠ Reasons:")

            for r in context.reasons:

                print(f" - {r}")

    # -------------------------------------------------
    # ACCOUNT
    # -------------------------------------------------

    def _print_account(self, account):

        print("\n💰 ACCOUNT")

        print("-" * 40)

        print(f"Capital     : {account.initial_capital}")

        print(f"Drawdown    : {account.drawdown:.2%}")

        print(f"Daily PnL   : {account.daily_pnl:.2f}")

    # -------------------------------------------------
    # POSITIONS
    # -------------------------------------------------

    def _print_positions(self, positions):

        print("\n📦 OPEN POSITIONS")

        print("-" * 40)

        if not positions:

            print("No open positions")

            return

        for p in positions:

            print(
                f"{p.symbol} | "
                f"Strike: {p.strike} | "
                f"Entry: {p.entry_price:.2f} | "
                f"PnL: {p.unrealized_pnl:.2f} | "
                f"Health: {p.trade_health:.1f}"
            )

    # -------------------------------------------------
    # CANDIDATES
    # -------------------------------------------------

    def _print_candidates(self, candidates):

        print("\n🎯 TOP CANDIDATES")

        print("-" * 40)

        if not candidates:

            print("No candidates found")

            return

        for c in candidates[:5]:

            print(
                f"{c.symbol} | "
                f"Strike: {c.strike} | "
                f"Score: {c.final_score:.2f}"
            )