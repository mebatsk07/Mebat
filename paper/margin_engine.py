from datetime import datetime

from paper.position import PaperPosition


class PaperBroker:

    def __init__(self, account):

        self.account = account

        self.positions = []

    # -------------------------

    def open_position(

        self,

        candidate,

        quantity,

        stop_loss,

        target_price,

    ):

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

            stop_loss=stop_loss,

            target_price=target_price,

            entry_time=datetime.now(),

        )

        self.positions.append(position)

        margin = candidate.premium * quantity

        self.account.margin_used += margin

        self.account.available_margin -= margin

        self.account.open_positions += 1

        self.account.total_trades += 1

        print()

        print("=" * 60)

        print("PAPER POSITION OPENED")

        print(position)

        print("=" * 60)

        return position

    # -------------------------

    def update_price(

        self,

        symbol,

        premium,

    ):

        for position in self.positions:

            if position.symbol != symbol:

                continue

            position.current_price = premium

            pnl = (

                position.entry_price

                - premium

            ) * position.quantity

            position.unrealized_pnl = pnl

            position.max_profit = max(

                position.max_profit,

                pnl,

            )

            position.max_loss = min(

                position.max_loss,

                pnl,

            )

    # -------------------------

    def close_position(

        self,

        symbol,

        exit_price,

        reason,

    ):

        for position in self.positions:

            if position.symbol != symbol:

                continue

            position.status = "CLOSED"

            position.exit_price = exit_price

            position.exit_time = datetime.now()

            pnl = (

                position.entry_price

                - exit_price

            ) * position.quantity

            position.realized_pnl = pnl

            self.account.realized_pnl += pnl

            if pnl > 0:

                self.account.winning_trades += 1

            else:

                self.account.losing_trades += 1

            margin = (

                position.entry_price

                * position.quantity

            )

            self.account.margin_used -= margin

            self.account.available_margin += margin

            self.account.open_positions -= 1

            print()

            print("=" * 60)

            print("POSITION CLOSED")

            print(reason)

            print("PnL:", pnl)

            print("=" * 60)