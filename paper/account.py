from dataclasses import dataclass

from config import strategy


@dataclass
class PaperAccount:

    # ----------------------------
    # Capital
    # ----------------------------

    starting_balance: float = strategy.ACCOUNT_CAPITAL

    balance: float = strategy.ACCOUNT_CAPITAL

    available_balance: float = strategy.ACCOUNT_CAPITAL

    margin_used: float = 0.0

    # ----------------------------
    # Profit & Loss
    # ----------------------------

    realized_pnl: float = 0.0

    unrealized_pnl: float = 0.0

    daily_pnl: float = 0.0

    total_pnl: float = 0.0

    # ----------------------------
    # Statistics
    # ----------------------------

    total_trades: int = 0

    winning_trades: int = 0

    losing_trades: int = 0

    # ----------------------------
    # Drawdown
    # ----------------------------

    highest_balance: float = strategy.ACCOUNT_CAPITAL

    maximum_drawdown: float = 0.0

    # --------------------------------------------------

    @property
    def equity(self):

        return self.balance + self.unrealized_pnl

    # --------------------------------------------------

    @property
    def win_rate(self):

        if self.total_trades == 0:

            return 0.0

        return (

            self.winning_trades

            / self.total_trades

        ) * 100