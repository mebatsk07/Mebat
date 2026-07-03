from datetime import datetime

from paper.paper_position import PaperPosition


# =====================================================
# PAPER BROKER
# =====================================================

class PaperBroker:

    def __init__(self, position_manager):

        self.position_manager = position_manager

        self.account = None  # can be injected later if needed

    # -------------------------------------------------
    # SELL OPTION (ENTRY)
    # -------------------------------------------------

    def sell_option(
        self,
        candidate,
        context,
        quantity=1,
        stop_loss=None,
        target=None,
    ):

        now = datetime.utcnow()

        position = PaperPosition(

            symbol=candidate.symbol,

            product_id=candidate.product_id,

            side="SELL",

            option_type=getattr(candidate, "option_type", ""),

            strike=candidate.strike,

            expiry=candidate.expiry,

            quantity=quantity,

            entry_price=candidate.premium,

            current_price=candidate.premium,

            stop_loss=stop_loss or 0,

            target_price=target or 0,

            entry_time=now,

            status="OPEN",

        )

        # add to position manager immediately
        self.position_manager.add_position(position)

        print()

        print("=" * 60)

        print("NEW PAPER TRADE OPENED")

        print("=" * 60)

        print(f"Symbol   : {position.symbol}")

        print(f"Strike   : {position.strike}")

        print(f"Entry    : {position.entry_price}")

        print(f"Quantity : {position.quantity}")

        print(f"Time     : {position.entry_time}")

        print("=" * 60)

        return position

    # -------------------------------------------------
    # CLOSE POSITION
    # -------------------------------------------------

    def close_position(
        self,
        position,
        exit_price,
        reason="",
    ):

        position.status = "CLOSED"

        position.exit_price = exit_price

        position.exit_time = datetime.utcnow()

        position.unrealized_pnl = (
            exit_price - position.entry_price
        ) * position.quantity

        position.exit_reason = reason

        print()

        print("=" * 60)

        print("POSITION CLOSED")

        print("=" * 60)

        print(f"Symbol : {position.symbol}")

        print(f"PnL    : {position.unrealized_pnl}")

        print(f"Reason : {reason}")

        print("=" * 60)

        return position