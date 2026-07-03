class PerformanceMetrics:

    def calculate(self, portfolio):

        trades = portfolio.closed_trades

        wins = [t for t in trades if t.pnl > 0]

        losses = [t for t in trades if t.pnl <= 0]

        win_rate = 0

        if trades:

            win_rate = len(wins) / len(trades) * 100

        total_profit = sum(t.pnl for t in wins)

        total_loss = abs(sum(t.pnl for t in losses))

        profit_factor = 0

        if total_loss:

            profit_factor = total_profit / total_loss

        return {

            "Trades": len(trades),

            "Win Rate": win_rate,

            "Profit Factor": profit_factor,

            "Net Profit": total_profit - total_loss,

            "Average Win":
                total_profit / max(len(wins), 1),

            "Average Loss":
                total_loss / max(len(losses), 1),
        }