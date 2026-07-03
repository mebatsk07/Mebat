from datetime import datetime

from database.repository import Repository
from database.models import PaperTrade, DecisionLog


class PaperJournal:

    def __init__(self):

        self.repo = Repository()

    # --------------------------------------------------
    # OPEN TRADE
    # --------------------------------------------------

    def open_trade(self, position, context):

        trade = PaperTrade(

            symbol=position.symbol,

            strike=position.strike,

            option_type=position.option_type,

            expiry=position.expiry,

            quantity=position.quantity,

            entry_time=datetime.now(),

            exit_time=None,

            entry_price=position.entry_price,

            exit_price=None,

            pnl=0,

            theta=0,

            iv_entry=context.atm_iv,

            iv_exit=None,

            rv=context.historical_volatility,

            pcr=context.pcr_oi,

            regime=context.regime,

            trend=context.trend,

            health_entry=100,

            health_exit=None,

            exit_reason=None,

            entry_delta=position.delta,

            exit_delta=None,

            entry_iv_rv=context.iv_rv_ratio,

            direction_confidence=context.confidence,

            trade_score=position.trade_score,

            stop_loss=position.stop_loss,

            target_price=position.target_price,

        )

        self.repo.save_paper_trade(trade)

    # --------------------------------------------------
    # CLOSE TRADE
    # --------------------------------------------------

    def close_trade(self, position, context, reason):

        trade = self.repo.get_open_trade(position.symbol)

        if trade is None:
            return

        trade.exit_time = datetime.now()

        trade.exit_price = position.current_price

        trade.pnl = position.pnl

        trade.theta = position.theta_captured

        trade.iv_exit = context.atm_iv

        trade.health_exit = position.trade_health

        trade.exit_reason = reason

        trade.exit_delta = position.delta

        self.repo.update_paper_trade(trade)

    # --------------------------------------------------
    # DECISION LOG
    # --------------------------------------------------

    def log_decision(
        self,
        candidate,
        score,
        decision,
        reason,
        context,
    ):

        log = DecisionLog(

            timestamp=datetime.now(),

            symbol=candidate.symbol,

            premium=candidate.premium,

            delta=candidate.delta,

            score=score,

            trend=context.trend,

            regime=context.regime,

            decision=decision,

            reason=reason,

        )

        self.repo.save_decision(log)

    # --------------------------------------------------
    # DAILY SUMMARY
    # --------------------------------------------------

    def daily_summary(self):

        return self.repo.daily_statistics()

    # --------------------------------------------------
    # CLOSE DATABASE
    # --------------------------------------------------

    def close(self):

        self.repo.close()