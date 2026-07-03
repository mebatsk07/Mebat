from datetime import datetime

from paper.account import PaperAccount
from paper.paper_position import PaperPosition
from paper.trading_journal import TradingJournal


class PaperBroker:

    def __init__(self, position_manager):

        self.account = PaperAccount()

        self.position_manager = position_manager

        self.journal = TradingJournal()

    # --------------------------------------------------
    # SELL OPTION
    # --------------------------------------------------

    def sell_option(

        self,

        candidate,

        context,

        quantity=1,

    ):

        margin = candidate.premium * quantity * 100

        # Check available balance
        if self.account.available_balance < margin:

            print("\nInsufficient account balance.")

            return None

        # Reserve margin
        self.account.available_balance -= margin
        self.account.margin_used += margin

        # Create paper position
        position = PaperPosition(

            symbol=candidate.symbol,

            product_id=candidate.product_id,

            side="SELL",

            option_type=candidate.option_type,

            strike=candidate.strike,

            expiry=candidate.expiry,

            quantity=quantity,

            entry_price=candidate.premium,

            current_price=candidate.premium,

            stop_loss=candidate.premium * 2,

            target_price=0,

            entry_time=datetime.utcnow(),

            status="OPEN",

        )

        # Add to Position Manager
        self.position_manager.add_position(position)

        # Update account statistics
        self.account.total_trades += 1

        print()
        print("=" * 70)
        print("PAPER TRADE OPENED")
        print("=" * 70)
        print(f"Symbol       : {position.symbol}")
        print(f"Strike       : {position.strike}")
        print(f"Option Type  : {position.option_type}")
        print(f"Entry Price  : {position.entry_price:.2f}")
        print(f"Quantity     : {position.quantity}")
        print(f"Margin Used  : {margin:.2f}")
        print("=" * 70)

        return position

    # --------------------------------------------------
    # CLOSE POSITION
    # --------------------------------------------------

    def close_position(

        self,

        position,

        exit_price,

        context,

        reason="",

    ):

        if position.status == "CLOSED":

            return

        position.status = "CLOSED"

        position.exit_price = exit_price

        position.exit_time = datetime.utcnow()

        position.exit_reason = reason

        pnl = (

            position.entry_price

            - exit_price

        ) * position.quantity * 100

        position.realized_pnl = pnl

        margin = (

            position.entry_price

            * position.quantity

            * 100

        )

        # Release margin
        self.account.margin_used -= margin

        self.account.available_balance += margin

        # Update balance
        self.account.balance += pnl

        self.account.realized_pnl += pnl

        self.account.daily_pnl += pnl

        self.account.total_pnl += pnl

        if pnl >= 0:

            self.account.winning_trades += 1

        else:

            self.account.losing_trades += 1

        # Highest Balance
        if self.account.balance > self.account.highest_balance:

            self.account.highest_balance = self.account.balance

        # Maximum Drawdown
        drawdown = (

            self.account.highest_balance

            - self.account.balance

        )

        if drawdown > self.account.maximum_drawdown:

            self.account.maximum_drawdown = drawdown

        # Save to trading journal
        self.journal.record(

            position,

            context,

        )

        print()
        print("=" * 70)
        print("POSITION CLOSED")
        print("=" * 70)
        print(f"Symbol       : {position.symbol}")
        print(f"Exit Price   : {exit_price:.2f}")
        print(f"PnL          : {pnl:.2f}")
        print(f"Reason       : {reason}")
        print("=" * 70)

    # --------------------------------------------------
    # ACCOUNT SUMMARY
    # --------------------------------------------------

    def account_summary(self):

        print()
        print("=" * 70)
        print("ACCOUNT SUMMARY")
        print("=" * 70)
        print(f"Balance            : {self.account.balance:.2f}")
        print(f"Available Balance  : {self.account.available_balance:.2f}")
        print(f"Margin Used        : {self.account.margin_used:.2f}")
        print(f"Equity             : {self.account.equity:.2f}")
        print(f"Daily PnL          : {self.account.daily_pnl:.2f}")
        print(f"Total PnL          : {self.account.total_pnl:.2f}")
        print(f"Trades             : {self.account.total_trades}")
        print(f"Win Rate           : {self.account.win_rate:.2f}%")
        print("=" * 70)