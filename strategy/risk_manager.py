from dataclasses import dataclass

from config import strategy


@dataclass
class RiskDecision:

    allowed: bool

    reason: str

    max_loss_usd: float

    contracts: int

    margin_required: float


class RiskManager:

    def evaluate(
        self,
        candidate,
        account_balance,
        deployed_capital,
        open_positions,
    ):

        # -----------------------------
        # Maximum Positions
        # -----------------------------

        if open_positions >= strategy.MAX_OPEN_POSITIONS:

            return RiskDecision(
                False,
                "Maximum open positions reached",
                0,
                0,
                0,
            )

        # -----------------------------
        # Capital Deployment
        # -----------------------------

        if deployed_capital >= strategy.DEPLOYED_CAPITAL:

            return RiskDecision(
                False,
                "Deployment limit reached",
                0,
                0,
                0,
            )

        # -----------------------------
        # Maximum Dollar Risk
        # -----------------------------

        max_loss = strategy.RISK_PER_TRADE_USD

        # -----------------------------
        # Estimate Margin
        # -----------------------------

        contract_value = candidate.spot * 0.001

        margin = contract_value / 200

        contracts = int(max_loss / margin)

        if contracts < 1:

            contracts = 1

        return RiskDecision(

            allowed=True,

            reason="Risk Approved",

            max_loss_usd=max_loss,

            contracts=contracts,

            margin_required=contracts * margin,
        )