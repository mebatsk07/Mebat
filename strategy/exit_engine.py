from datetime import datetime


class ExitEngine:

    def evaluate(
        self,
        position,
        market_context,
        account,
    ):

        # -----------------------------
        # 1. Emergency Account Stop
        # -----------------------------

        if account.max_drawdown >= 5:
            return True, "Maximum drawdown reached"

        # -----------------------------
        # 2. Daily Loss
        # -----------------------------

        if account.daily_pnl <= -1500:
            return True, "Daily loss limit"

        # -----------------------------
        # 3. Stop Loss
        # -----------------------------

        if position.current_price >= position.stop_loss:
            return True, "Stop Loss"

        # -----------------------------
        # 4. Profit Target
        # -----------------------------

        if position.current_price <= position.target_price:
            return True, "Profit Target"

        # -----------------------------
        # 5. Expiry
        # -----------------------------

        if market_context.hours_to_expiry <= 6:
            return True, "Less than 6 hours to expiry"

        # -----------------------------
        # 6. Trend Reversal
        # -----------------------------

        if position.option_type == "put_options":

            if market_context.trend == "UP":
                return True, "Trend reversed"

        if position.option_type == "call_options":

            if market_context.trend == "DOWN":
                return True, "Trend reversed"

        # -----------------------------
        # 7. IV Spike
        # -----------------------------

        if market_context.iv_rv_ratio > 2.0:
            return True, "Volatility spike"

        # -----------------------------
        # 8. OI Reversal
        # -----------------------------

        if market_context.direction_confidence < 60:
            return True, "OI reversal"

        return False, "Hold Position"