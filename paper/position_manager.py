from dataclasses import dataclass
from typing import List, Optional

from paper.paper_position import PaperPosition


# =====================================================
# POSITION MANAGER
# =====================================================

class PositionManager:

    def __init__(self):

        self.positions: List[PaperPosition] = []

    # -------------------------------------------------
    # ADD POSITION
    # -------------------------------------------------

    def add_position(self, position: PaperPosition):

        self.positions.append(position)

    # -------------------------------------------------
    # GET OPEN POSITIONS
    # -------------------------------------------------

    def get_open_positions(self) -> List[PaperPosition]:

        return [
            p for p in self.positions
            if p.status == "OPEN"
        ]

    # -------------------------------------------------
    # UPDATE POSITION PRICES
    # -------------------------------------------------

    def update(self, context):

        for position in self.get_open_positions():

            self._update_position(position, context)

    # -------------------------------------------------
    # INTERNAL UPDATE LOGIC
    # -------------------------------------------------

    def _update_position(self, position: PaperPosition, context):

        # simulate current price from market context
        # (for now: simple approximation using spot movement)

        spot = context.spot

        # simplified mark-to-market
        position.current_price = position.entry_price * (
            1 + (spot - position.strike) / position.strike * 0.01
        )

        # PnL calculation (SELL strategy)
        position.unrealized_pnl = (
            position.entry_price - position.current_price
        ) * position.quantity

        # update max profit / loss tracking
        if position.unrealized_pnl > position.max_profit:
            position.max_profit = position.unrealized_pnl

        if position.unrealized_pnl < position.max_loss:
            position.max_loss = position.unrealized_pnl

        # trade health scoring
        self._update_trade_health(position)

    # -------------------------------------------------
    # TRADE HEALTH SYSTEM
    # -------------------------------------------------

    def _update_trade_health(self, position: PaperPosition):

        pnl_ratio = (
            position.unrealized_pnl /
            (position.entry_price * position.quantity)
            if position.entry_price > 0 else 0
        )

        health = 100

        # penalty for drawdown
        if pnl_ratio < -0.02:
            health -= 20

        if pnl_ratio < -0.05:
            health -= 40

        if position.unrealized_pnl < 0:
            health -= 10

        # reward for profit
        if pnl_ratio > 0.03:
            health += 10

        if pnl_ratio > 0.05:
            health += 20

        position.trade_health = max(0, min(100, health))

    # -------------------------------------------------
    # CLOSE POSITION
    # -------------------------------------------------

    def close_position(self, position: PaperPosition, exit_price: float, reason: str = ""):

        position.status = "CLOSED"

        position.exit_price = exit_price

        position.unrealized_pnl = (
            exit_price - position.entry_price
        ) * position.quantity

        position.exit_reason = reason

        return position

    # -------------------------------------------------
    # GET TOTAL PNL
    # -------------------------------------------------

    def total_pnl(self) -> float:

        return sum(
            p.unrealized_pnl
            for p in self.positions
        )

    # -------------------------------------------------
    # SUMMARY
    # -------------------------------------------------

    def summary(self):

        open_positions = self.get_open_positions()

        return {

            "open_positions": len(open_positions),

            "total_positions": len(self.positions),

            "total_pnl": self.total_pnl(),

            "avg_trade_health": (
                sum(p.trade_health for p in open_positions) /
                len(open_positions)
                if open_positions else 0
            ),

        }