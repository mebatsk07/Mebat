from dataclasses import dataclass


@dataclass
class PortfolioRisk:

    approved: bool

    reason: str

    total_delta: float

    total_gamma: float

    total_theta: float

    total_vega: float


class PortfolioRiskEngine:

    MAX_DELTA = 0.20

    MAX_GAMMA = 0.01

    MAX_VEGA = 100

    def evaluate(self, open_positions, new_candidate):

        delta = 0
        gamma = 0
        theta = 0
        vega = 0

        for p in open_positions:

            delta += p.delta

            gamma += p.gamma

            theta += p.theta

            vega += p.vega

        delta += new_candidate.delta
        gamma += new_candidate.gamma
        theta += new_candidate.theta
        vega += new_candidate.vega

        if abs(delta) > self.MAX_DELTA:

            return PortfolioRisk(
                False,
                "Portfolio Delta Limit",
                delta,
                gamma,
                theta,
                vega,
            )

        if abs(gamma) > self.MAX_GAMMA:

            return PortfolioRisk(
                False,
                "Portfolio Gamma Limit",
                delta,
                gamma,
                theta,
                vega,
            )

        if abs(vega) > self.MAX_VEGA:

            return PortfolioRisk(
                False,
                "Portfolio Vega Limit",
                delta,
                gamma,
                theta,
                vega,
            )

        return PortfolioRisk(
            True,
            "Approved",
            delta,
            gamma,
            theta,
            vega,
        )