from paper.paper_position import PaperPosition


class PaperBroker:

    def __init__(self):

        self.positions = []

    def sell_option(
        self,
        candidate,
        quantity,
        stop_loss,
        target,
    ):

        position = PaperPosition(

            symbol=candidate.symbol,

            side="SELL",

            quantity=quantity,

            entry_price=candidate.premium,

            current_price=candidate.premium,

            stop_loss=stop_loss,

            target=target,

            entry_time=None,

            expiry=None,
        )

        self.positions.append(position)

        print()

        print("=" * 50)

        print("PAPER TRADE OPENED")

        print(position)

        print("=" * 50)

        return position