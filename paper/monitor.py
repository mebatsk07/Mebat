from strategy.exit_engine import ExitEngine
from strategy.trade_health import TradeHealthEngine


class PositionMonitor:

    def __init__(
        self,
        account,
        broker,
        journal,
    ):

        self.account = account

        self.broker = broker

        self.journal = journal

        self.exit_engine = ExitEngine()

        self.trade_health = TradeHealthEngine()

    # --------------------------------------------------
    # Update all positions
    # --------------------------------------------------

    def update(self, context):

        positions = self.broker.position_manager.get_open_positions()

        for position in positions:

            self.update_price(position)

            self.update_pnl(position)

            self.update_theta(position)

            self.update_health(position, context)

            self.check_exit(position, context)

    # --------------------------------------------------
    # Premium
    # --------------------------------------------------

    def update_price(self, position):

        latest = self.broker.get_latest_price(position.symbol)

        position.current_price = latest

    # --------------------------------------------------
    # PnL
    # --------------------------------------------------

    def update_pnl(self, position):

        position.unrealized_pnl = (

            position.entry_price -

            position.current_price

        ) * position.quantity

    # --------------------------------------------------
    # Theta
    # --------------------------------------------------

    def update_theta(self, position):

        position.theta_captured = (

            position.entry_price -

            position.current_price

        )

    # --------------------------------------------------
    # Trade Health
    # --------------------------------------------------

    def update_health(

        self,

        position,

        context,

    ):

        position.trade_health = (

            self.trade_health.calculate(

                position,

                context,

            )

        )

    # --------------------------------------------------
    # Exit
    # --------------------------------------------------

    def check_exit(

        self,

        position,

        context,

    ):

        should_exit, reason = (

            self.exit_engine.evaluate(

                position,

                context,

                self.account,

            )

        )

        if should_exit:

            self.broker.close_position(

                position,

                reason,

            )

            self.journal.close_trade(

                position,

                context,

                reason,

            )