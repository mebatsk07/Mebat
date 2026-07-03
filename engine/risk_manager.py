from dataclasses import dataclass


# =====================================================
# RISK RESULT
# =====================================================

@dataclass
class RiskResult:

    allowed: bool

    reason: str


# =====================================================
# RISK MANAGER
# =====================================================

class RiskManager:

    def __init__(self):

        self.max_positions = 2

        self.max_drawdown = 0.05  # 5%

        self.max_daily_loss = 0.03  # 3%

        self.min_score = 60

        self.max_exposure_per_trade = 0.5  # 50% of capital

    # -------------------------------------------------
    # MAIN VALIDATION
    # -------------------------------------------------

    def validate(
        self,
        candidate,
        context,
        account,
        position_manager,
    ):

        # =================================================
        # 1. POSITION LIMIT CHECK
        # =================================================

        open_positions = position_manager.get_open_positions()

        if len(open_positions) >= self.max_positions:

            return RiskResult(
                False,
                "Max open positions reached"
            )

        # =================================================
        # 2. MARKET QUALITY CHECK
        # =================================================

        if not context.trade_allowed:

            return RiskResult(
                False,
                f"Market filter blocked trade: {context.reasons}"
            )

        # =================================================
        # 3. SCORE CHECK
        # =================================================

        if candidate.final_score < self.min_score:

            return RiskResult(
                False,
                "Candidate score too low"
            )

        # =================================================
        # 4. DRAWDOWN CHECK
        # =================================================

        if account.drawdown >= self.max_drawdown:

            return RiskResult(
                False,
                "Max drawdown limit hit"
            )

        # =================================================
        # 5. DAILY LOSS CHECK
        # =================================================

        if account.daily_pnl <= -self.max_daily_loss * account.initial_capital:

            return RiskResult(
                False,
                "Daily loss limit hit"
            )

        # =================================================
        # 6. EXPOSURE CHECK
        # =================================================

        exposure = sum(
            pos.entry_price * pos.quantity
            for pos in open_positions
        )

        max_allowed = account.initial_capital * self.max_exposure_per_trade

        if exposure >= max_allowed:

            return RiskResult(
                False,
                "Exposure limit exceeded"
            )

        # =================================================
        # 7. FINAL APPROVAL
        # =================================================

        return RiskResult(
            True,
            "Trade approved"
        )